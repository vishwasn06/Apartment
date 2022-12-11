
from django.contrib import admin
from account.models import Profile, User, Guest, Resident
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('id','email','is_guest','is_resident','first_name','last_name','phone_number')
    search_fields = ('id','email','username')


admin.site.register(User, AccountAdmin)
admin.site.register(Guest)
admin.site.register(Resident)
admin.site.register(Profile)