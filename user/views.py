from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            user_name=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {user_name}, Account Created Successfully ! ')
            return redirect('coreapp:index')
    else:
        form=forms.SigninForm()
    context={'form':form}
    return render(request,'user/signup.html',context)

@login_required
def profile(request):
    return render(request,'user/profile_page.html')

@login_required
def update_profile(request):
    if request.user.userprofile and request.method == 'POST':
         form = forms.ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
         if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated Successfully !')
            return redirect('user:profile')
         else:
            print(form.errors)
            messages.error(request,'Please Enter Correct Data !')
    else:
        form = forms.ProfileForm(instance=request.user.userprofile)
    context={'form':form }  
    return render(request,'user/profile_form.html',context)


