#Django
from django.db import models

from User.models import User, UserProfile


#Enterprise info
class EnterpriseProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, primary_key=True)
    enterprise_register_date = models.DateField(default=None, auto_now_add=True)
    business_name = models.CharField(max_length=250, default=None, null=False, blank=False)
    tax_regime = models.CharField(max_length=250, default=None, null=False, blank=True)
    enterprise_email = models.EmailField(unique=True, null=True, blank=True)
    enterprise_phone_number = models.DecimalField(max_digits=16, unique=False, null=True, blank=True)
    enterprise_date_of_birth = models.DateField(default=None, null=True)
    enterprice_place_of_birth = models.CharField(max_length=64, blank=True)
    enterprice_country = models.CharField(max_length=64, blank=True)
    rfc = models.CharField(max_length=15, unique=True, null=True)
    description = models.CharField(max_length=250, blank=True)
    enterprise_profile_image = models.OneToOneField(UserImage, on_delete=models.PROTECT,
                                              related_name="enterprise_profile")

    def __str__(self):
        return
    
class Membership(models.Model):
    enterprise_membership = models.ForeignKey(EnterpriseProfile, on_delete=models.CASCADE,
                              related_name='enterprise_user'))
    type_membership = models.CharField(max_length=3, default=None, blank=True)
    
    def __str__(self):
        return
   
class EnterpriseAddress(models.Model):
    country = models.CharField(max_length=100, default=None, blank=True)
    address_province = models.CharField(max_length=100, default=None, blank=True)
    address_city = models.CharField(max_length=100, default=None, blank=True)
    address_suburb = models.CharField(max_length=100, default=None, blank=True)
    address_street = models.CharField(max_length=500, default=None, blank=True)
    address_int_number = models.CharField(max_length=500, default=None, blank=True)
    postal_code = models.CharField(max_length=10, default=None, blank=True)

    def __str__(self):
        return self.country, self.address_street


class Scoring(models.Model):
    value = models.CharField(max_length=100, default=None, blank=True)
    comment = models.CharField(max_length=1000, default=None, blank=True)
    status = 

    def __str__(self):
        return self.value, self.comment
    
    
class EnterpriseCalendar(models.Model):
   inicial_date = models.DateField(default=None, auto_now_add=False)
   termination_date = models.DateField(default=None, auto_now_add=False)
   duration_time = models.DateField(default=None, null=True)
   
   def __str__(self):
       return self.inicial_date