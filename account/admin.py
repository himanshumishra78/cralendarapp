from django.contrib import admin

# Register your models here.
from .models import UserReg
# Register your models here.
@admin.register(UserReg)
class UserRegAdmin(admin.ModelAdmin):
    list=['user','mobile_num',]
