from django.contrib import admin
from .models import Profile, Consumer, Store
# Register your models here.
# admin.site.register(User)
admin.site.register(Consumer)
admin.site.register(Store)
admin.site.register(Profile)