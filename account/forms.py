from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import Guest, Profile, Resident, User
from django.contrib.auth import get_user_model
User = get_user_model()

class GuestSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    aadhar = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guest = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        guest = Guest.objects.create(user=user)

        
        guest.aadhar = self.cleaned_data.get('aadhar')
        guest.save()
        return user


class ResidentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    aadhar = forms.CharField(required=True)
    phone_number = forms.CharField(required=True, help_text='Required. Add a valid phone number .' )
    Room = forms.IntegerField(required=True, help_text='Required.Add assgined Room Number .' )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_resident = True
        user.is_staff = False
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        resident = Resident.objects.create(user=user)
        resident.aadhar = self.cleaned_data.get('aadhar')
        resident.Room = self.cleaned_data.get('Room')
        resident.save()
        return user



class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(phone_number=phone_number)
        except User.DoesNotExist:
            return phone_number
        raise forms.ValidationError('phone"%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


