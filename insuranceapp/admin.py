from django.contrib import admin
from .models import UserData
from .models import custdata
from .models import Contact

admin.site.register(custdata)
admin.site.register(UserData)
admin.site.register(Contact)