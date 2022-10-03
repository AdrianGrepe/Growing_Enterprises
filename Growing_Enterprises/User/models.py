#Django
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

#Utilities
# from Enterprise.models import EnterpriseProfile


class UserImage(models.Model):
    ''' 
    Upload all user images and its description:
    Profile image, description image and other image.
    ''' 
    profile_image = models.FileField(upload_to='user/profile_image', default=None) #created in your database as varchar columns with a default max length of 100 characters
    description_image = models.FileField(upload_to='user/description_image', default=None)
    other_image = models.FileField(upload_to='user/other_image', default=None)
    
    
#Properties of the user
class UserProfile(models.Model):

    GENDERS = (
        ('Female', 'Femenino'),
        ('Male', 'Masculino'),
        ('Other', 'Otro'),
    )

    '''
    Properties of the user:
    User name, register date, phone number, lada (in case), date of birth,
    rfc, emal, full name, address, country, gender, status and
    user profile image
    '''
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    user_register_date = models.DateField(auto_now_add=True)
    user_phone_number = models.DecimalField(_("número de telefono"), max_digits=15, decimal_places=2, default=None, null=True)
    foreign_lada = models.DecimalField(_("lada"), max_digits=5, decimal_places=0, default=None, null=True, blank=True)
    date_of_birth = models.DateField(_("fecha de nacimiento"), default=None,null=True)
    user_rfc = models.CharField(_("RFC"), max_length=18, unique=True, null=True)
    user_email = models.EmailField(_("correo electrónico"), unique=True, null=False, blank=False)

    user_name = models.CharField(_("nombre"), max_length=100, null=False, blank=False)
    user_last_name = models.CharField(_("apellido"), max_length=100, null=False, blank=False)

    user_address = models.CharField(max_length=500, null=True, blank=True)
    user_country = models.CharField(max_length=40, null=True, blank=True)
    user_gender = models.CharField(max_length=6, blank=True, choices=GENDERS)
    status = models.CharField(max_length=40, null=True, blank=True)
    user_profile_image = models.OneToOneField(UserImage, on_delete=models.PROTECT,
                                              related_name="user_profile") #a one to one relationship

    
    class Meta:
        ordering = ["user_email"]
        verbose_name = _("perfil")
        verbose_name_plural = _("perfiles")


    def __str__(self):
      return f'{self.user} {self.user_email}'