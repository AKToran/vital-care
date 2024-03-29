from rest_framework import viewsets
from rest_framework.views import APIView
from .import models
from django.contrib.auth.models import User
from . serializers import PatientSerializer, RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = PatientSerializer

class RegistrationApiView(APIView): 
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            verify_link = f"http://127.0.0.1:8000/patient/activate/{uid}/{token}"
            email_subject = "Verify Email"
            email_body = render_to_string('verify_email.html', {'verify_link': verify_link})
            email = EmailMultiAlternatives(email_subject,'', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response('Check your mail for verification.')
        
        return Response(serializer.errors)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
class LoginApiView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
                #! gives error: Object of type Token is not JSON serializable IF SENDING TOKEN. token.key fixes it.
            else:
                return Response({'error': 'Invalid username or password!'})
        return Response(serializer.errors)

class LogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    

