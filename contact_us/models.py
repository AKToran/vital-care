from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    problem = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self) -> str:
        return f"Complaint of {self.name}"
    

