#Django
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User, Group

#Utilities
from Enterprise.models import EnterpriseProfile

#Uploading all photos 
class UserImage(models.Model):
    #TODO falta agregar la direccion del archivo
    profile_image = models.FileField(upload_to='User', default=None)
    description_image = models.FileField(upload_to='User', default=None)
    other_image = models.FileField(upload_to='User', default=None)
    
    
#Properties of the user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    user_register_date = models.DateField(default=None, auto_now_add=True)
    user_phone_number = models.DecimalField(max_digits=15, default=None, null=True)
    foreign_lada = models.DecimalField(max_digits=3, default=None, null=True, blank=True)
    date_of_birth = models.DateField(default=None,null=True)
    user_rfc = models.CharField(max_length=18, unique=True, null=True)
    user_email = models.EmailField(unique=True, null=False, blank=False)
    user_full_name = models.CharField(max_length=250, null=False, blank=False)
    user_address = models.CharField(max_length=500, null=True, blank=True)
    user_country = models.CharField(max_length=40, null=True, blank=True)
    user_gender = models.CharField(max_length=6, blank=True)
    status = models.CharField(max=40, null=True, blank=True)
    user_profile_image = models.OneToOneField(UserImage, on_delete=models.PROTECT,
                                              related_name="user_profile")
    
    def __str__(self):
      return self.user, self.email
    


   
