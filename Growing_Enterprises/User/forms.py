#  Python
import datetime
from pycountry import countries
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
from decimal import Decimal

# Django
from django import forms
from django.forms import ModelForm, DateField
from django.contrib.auth.models import User, Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Models
from .models import UserProfile, UserImage


AREA_CODES = [('+'+str(c),'+'+str(c)) for c in COUNTRY_CODE_TO_REGION_CODE.keys()]
COUNTRIES = [(str(c.name), str(c.name)) for c in countries]


class UserRegisterForm (ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            'user_email',
            'user_name',
            'user_last_name',
            'foreign_lada',
            'user_phone_number',
            'date_of_birth',
            'user_gender',
            'user_address',
            'user_country',
            'user_rfc',
        ]

        field_classes = {
            # 'slug': MySlugFormField,
        }

        labels = {
            'user_email': _('Correo electrónico'),
            'user_name': _('Nombre(s)'),
            'user_last_name': _('Apellidos(s)'),
            'foreign_lada': _('Lada'),
            'user_phone_number': _('Número de telefono'),
            'date_of_birth': _('Fecha de Nacimiento'),
            'user_gender': _('Género'),
            'user_address': _('Dirección completa'),
            'user_country': _('País'),
            'user_rfc': _('RFC'),
        }
        help_texts = {
            # 'user_phone_number': _('Número fijo o móvil.'),
        }
        error_messages = {
            'user_name': {
                'max_length': _("Nombre demasiado largo."),
            },
            'user_last_name': {
                'max_length': _("Nombre demasiado largo."),
            },
            'user_phone_number': {
                'max_length': _("Número invalido."),
            },
        }
        field_classes = {
            # 'user_phone_number': forms.IntegerField()
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'foreign_lada': forms.Select(choices=AREA_CODES,),
            'user_country': forms.Select(choices=COUNTRIES,),
            'user_phone_number': forms.TextInput(),
        }
        

    def clean_user_phone_number(self):
        phone_number = str(self.cleaned_data['user_phone_number'])
        if phone_number.isnumeric():
            phone_number = Decimal(phone_number)
            return phone_number

    
    def save(self):

        # Pass commit=False to return the unsaved model instances:

        # don't save to the database
        # >>> instances = formset.save(commit=False)
        # >>> for instance in instances:
        # ...     # do something with instance
        # ...     instance.save()
        # This gives you the ability to attach data to the instances before saving them to the database. If your formset contains a ManyToManyField, you’ll also need to call formset.save_m2m() to ensure the many-to-many relationships are saved properly.

        # After calling save(), your model formset will have three new attributes containing the formset’s changes:

        user = User.objects.create(
            username = self.cleaned_data.get('user_email'),
            email = self.cleaned_data.get('user_email'),
            first_name = self.cleaned_data.get('user_name'),
            last_name = self.cleaned_data.get('user_last_name'),
            is_active= False ,
        )
        
        user_profile_image=UserImage.objects.create()
        user_profile_image.save()

        user_profile = UserProfile.objects.create(
            user_email = self.cleaned_data.get('user_email'),
            user_name = self.cleaned_data.get('user_name'),
            user_last_name = self.cleaned_data.get('user_last_name'),
            foreign_lada = self.cleaned_data.get('foreign_lada'),
            user_phone_number = self.cleaned_data.get('user_phone_number'),
            date_of_birth = self.cleaned_data.get('date_of_birth'),
            user_gender = self.cleaned_data.get('user_gender'),
            user_address = self.cleaned_data.get('user_address'),
            user_country = self.cleaned_data.get('user_country'),
            user_rfc = self.cleaned_data.get('user_rfc'),
            user = user,
            user_profile_image = user_profile_image
        )
        user_profile.save()


        # return super().save(commit)

    
class EditProfileForm (ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            'user_email',
            'user_name',
            'user_last_name',
            'foreign_lada',
            'user_phone_number',
            'date_of_birth',
            'user_gender',
            'user_address',
            'user_country',
            'user_rfc',
        ]

        field_classes = {
            # 'slug': MySlugFormField,
        }

        labels = {
            'user_email': _('Correo electrónico'),
            'user_name': _('Nombre(s)'),
            'user_last_name': _('Apellidos(s)'),
            'foreign_lada': _('Lada'),
            'user_phone_number': _('Número de telefono'),
            'date_of_birth': _('Fecha de Nacimiento'),
            'user_gender': _('Género'),
            'user_address': _('Dirección completa'),
            'user_country': _('País'),
            'user_rfc': _('RFC'),
        }
        help_texts = {
            # 'user_phone_number': _('Número fijo o móvil.'),
        }
        error_messages = {
            'user_name': {
                'max_length': _("Nombre demasiado largo."),
            },
            'user_last_name': {
                'max_length': _("Nombre demasiado largo."),
            },
            'user_phone_number': {
                'max_length': _("Número invalido."),
            },
        }
        field_classes = {
            # 'user_phone_number': forms.IntegerField()
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'foreign_lada': forms.Select(choices=AREA_CODES,),
            'user_country': forms.Select(choices=COUNTRIES,),
            'user_phone_number': forms.TextInput(),
        }
        

    def clean_user_phone_number(self):
        phone_number = str(self.cleaned_data['user_phone_number'])
        if phone_number.isnumeric():
            phone_number = Decimal(phone_number)
            return phone_number


    # Not on forms
    # user = models.OneToOneField
    # user_register_date = models.DateField
    # status = models.CharField
    # user_profile_image = models.OneToOneField

    # Form fields
    # user_first_name = models.CharField
    # user_second_name = models.CharField
    # user_last_name = models.CharField
    # user_last_name_2 = models.CharField
    # user_phone_number = models.DecimalField
    # foreign_lada = models.DecimalField
    # date_of_birth = models.DateField
    # user_rfc = models.CharField
    # user_email = models.EmailField
    # user_address = models.CharField
    # user_country = models.CharFielduser_gender = models.CharField