#Django
from django.db import models

#Utilities
from User.models import User, UserProfile, UserImage


class EnterpriseProfile(models.Model):
    '''
    Enterprise information:
    Name, register date, tax regime (SA de CV, SA, etc), enterprise email,
    phone number, date of birth, place of birth, country, rfc, description,
    profile image, activity. 

    '''
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True) #A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.
    enterprise_register_date = models.DateField(auto_now_add=True) #register date of the company
    # A string field, business name
    business_name = models.CharField(max_length=250, default=None, null=False, blank=False) 
    tax_regime = models.CharField(max_length=250, default=None, null=False, blank=True)
    enterprise_email = models.EmailField(unique=True, null=True, blank=True)
    enterprise_phone_number = models.DecimalField(decimal_places=2, max_digits=16, unique=False, null=True, blank=True)
    enterprise_date_of_birth = models.DateField(default=None, null=True)

    enterprise_place_of_birth = models.CharField(max_length=64, blank=True)
    enterprise_country = models.CharField(max_length=64, blank=True)
    enterprise_activity = models.CharField(max_length=64, blank=True)
    rfc = models.CharField(max_length=15, unique=True, null=True)
    description = models.CharField(max_length=250, blank=True)
    enterprise_profile_image = models.OneToOneField(UserImage, on_delete=models.PROTECT,
                                              related_name="enterprise_profile")

    def __str__(self):
        return
    
class Membership(models.Model):

    '''
    Details of the membership plan:
    Profile, time, and price
    '''
    enterprise_membership = models.OneToOneField(EnterpriseProfile, on_delete=models.CASCADE,
                              related_name='enterprise_user')
    type_membership = models.CharField(max_length=3, default=None, blank=True)
    price_membership = models.DecimalField(decimal_places=2, max_digits=3, default=None, blank=True)

    
    def __str__(self):
        return self.type_membership

class EnterpriseAddress(models.Model): 
    '''
    Address of the company:
    Country, Province, city, suburb, street, int number, postal code.
    '''


    country = models.CharField(max_length=100, default=None, blank=True)
    province = models.CharField(max_length=100, default=None, blank=True)
    city = models.CharField(max_length=100, default=None, blank=True)
    suburb = models.CharField(max_length=100, default=None, blank=True)
    address_street = models.CharField(max_length=500, default=None, blank=True)
    address_int_number = models.CharField(max_length=500, default=None, blank=True)
    postal_code = models.CharField(max_length=10, default=None, blank=True)

    def __str__(self):
        return self.country, self.address_street


class Scoring(models.Model): 
    '''
    Inputs for scoring enterprise:
    value of the enterprise, coments, status.
    '''

    value = models.CharField(max_length=100, default=None, blank=True)
    comment = models.CharField(max_length=1000, default=None, blank=True)
    status = models.CharField(max_length=20, default=None, blank=True)

    def __str__(self):
        return self.value, self.comment
    
    

class EnterpriseCalendar(models.Model): 
    '''
    Calendar for events:
    Initial date, termination date, duration of the event (in hours)
    '''
    initial_date = models.DateField(default=None, auto_now_add=False)
    final_date = models.DateField(default=None, auto_now_add=False)
    duration_time = models.TimeField(default=None, null=True)

   
    def __str__(self):
       return self.inicial_date, self.final_date