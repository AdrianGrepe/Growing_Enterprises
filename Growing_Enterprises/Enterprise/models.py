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
   address
   status

   def __str__(self):
      return