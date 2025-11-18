from django.contrib import admin
from .models import UserData
from .models import custdata

admin.site.register(custdata)
admin.site.register(UserData)