from django.contrib import admin
from . import models

admin.site.register(models.AvailableTime)
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Doctor)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(models.Specialization, SpecializationAdmin)

admin.site.register(models.Review)