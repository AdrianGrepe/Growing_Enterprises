from django.contrib import admin
from .models import (
    EnterpriseProfile, Membership, EnterpriseAddress, Scoring, EnterpriseCalendar
)

# Register your models here.

admin.site.register(EnterpriseProfile)
admin.site.register(Membership)
admin.site.register(EnterpriseAddress)
admin.site.register(Scoring)
admin.site.register(EnterpriseCalendar)