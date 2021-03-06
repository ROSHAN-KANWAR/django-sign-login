from django.shortcuts import render
from .forms import regi,log,profile_admin,profile_user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.http import HttpResponseRedirect
# signup
def sign_up(request):
    if request.method == 'POST':
        fm = regi(request.POST)
        if fm.is_valid():
            fm.save()
            return  HttpResponseRedirect('/login')
    else:
       fm = regi()
    return render(request, 'signup.html', {'form': fm})
#login form

def user_login(request):
    if request.method == 'POST':
        fm = log(request=request, data=request.POST)
        if fm.is_valid():
            uname1 = fm.cleaned_data['username']
            upass1 = fm.cleaned_data['password']
            user = authenticate(username=uname1, password=upass1)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = log()
    return render(request, 'login.html', {'form': fm})
#profile
def Profile(request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                if request.user.is_superuser == True:
                    fm = profile_admin(request.POST, instance=request.user)
                    user = User.objects.all()
                else:
                    fm = profile_user(request.POST, instance=request.user)
                    user = None
                if fm.is_valid():
                    fm.save()

                    return HttpResponseRedirect('/profile/')
            else:
                if request.user.is_superuser == True:
                    fm = profile_admin(instance=request.user)
                    user = User.objects.all()
                else:

                    fm = profile_user(instance=request.user)
                    user = None
            return render(request, 'profile.html', {'name': fm, 'user': user})
        else:
            return HttpResponseRedirect('/')

#logout

def Logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')

#passwaord change

def user_change1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'change1.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
