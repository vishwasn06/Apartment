from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import  AccountUpdateForm, GuestSignUpForm, ProfileUpdateForm, ResidentSignUpForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
User = get_user_model()

def register(request):
    return render(request, 'account/register.html')

class guest_register(CreateView):
    model = User
    form_class = GuestSignUpForm
    template_name = 'account/guest_registrer.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home3')

class resident_register(CreateView):
    model = User
    form_class = ResidentSignUpForm
    template_name = 'account/resident_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if user.is_resident:
                        return redirect('/')
                else:
                    return redirect('home3')
        
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
            
    return render(request, 'account/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')


def account_view(request):
    
	if not request.user.is_authenticated:
		return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
                    "phone_number": request.POST['phone_number'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
                    "phone_number": request.user.phone_number,
				}
			)
	context['account_form'] = form
	return render(request, "account/account.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = AccountUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = AccountUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }

#     return render(request, 'account/profile.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'testprofile.html', context)

def newprofile(request):
    return render(request, 'account/style.html')



