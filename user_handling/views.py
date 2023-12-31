from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from stackapp.models import UserProfile
from django.contrib.auth.models import User
from .forms import UserForm,UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView





# Create your views here.


def activateEmail(request ,user ,profile ,email):
    messages.success(request , f'dear <b>{user}</b> , please go to your email <b>{email}</b>')





def user_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # email = user.get("email")
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.is_email_activated = False
            activateEmail(request ,user ,profile ,user_form.cleaned_data['email'])
            profile.save()
            
            return redirect('user_handling:user_login')
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered':registered,
    }
    
    return render(request, 'user_handling/register.html', context)



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username ,password =password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'index' with the appropriate URL name or path
        else:
            messages.error(request, 'Invalid username or password.')




    return render(request,'user_handling/login.html',{})


@login_required
def user_logout(request):
    logout(request)
    # Redirect to the desired page after logout
    return redirect('index')



@login_required
def user_detail(request):
    user= request.user
    context = {"user":user}
    #user_obj = get_object_or_404(User, id=user_id)
    
    return render(request, "user_handling/userprofile.html", context)


def publicuser(request):
    users = UserProfile.objects.filter(public =True)
    context = {"users":users}
    return render(request , "user_handling/publicuser.html",context)
