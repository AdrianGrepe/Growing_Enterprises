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

# class UserImagesForm (ModelForm):

#     class Meta:
#         model = UserImage
#         fields = '__all__'

class UserProfileForm (ModelForm):

    class Meta:

        AREA_CODES = [('+'+str(c),'+'+str(c)) for c in COUNTRY_CODE_TO_REGION_CODE.keys()]
        COUNTRIES = [(str(c.name), str(c.name)) for c in countries]

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

        name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        user = User.objects.create(
            username = self.cleaned_data.get('user_email'),
            email = self.cleaned_data.get('user_email'),
            name = self.cleaned_data.get('first_name'),
            last_name = self.cleaned_data.get('last_name'),
            is_valid = False ,
        )

        'user_email'
        'user_name'
        'user_last_name'
        'foreign_lada'
        'user_phone_number'
        'date_of_birth'
        'user_gender'
        'user_address'
        'user_country'
        'user_rfc'
        

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
        )


        # return super().save(commit)


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