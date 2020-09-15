from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form, UpdataUserForm, UserCreationForms, UpdateProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required




# Create your views here.
def doctor_lists(request):
    doctors = User.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'index.html', context)

def doctors_detail(request, slug):
    doctors_detail = Profile.objects.get(slug=slug)

    context = {
        'doctors_detail': doctors_detail
    }
    return render(request, 'doctors_detail.html', context)

def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:doctor_list')
    else:
        form = Login_Form()

    context ={
        'form': form
    }
    return render(request, 'login.html', context)


def signup(request):
    form = UserCreationForms()
    if request.method == 'POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:doctor_list')

        else:
            form = UserCreationForms()
    context = {

        'form': form
    }
    return render(request, 'signup.html', context)




@login_required()
def profile(request):

    return render(request, 'profile.html')



def updata_profile(request):
    user_form = UpdataUserForm(instance=request.user)
    profile_form = UpdateProfile(instance=request.user.profile)

    if request.method == "POST":
        user_form = UpdataUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()

            return redirect('accounts:doctor_list')
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'updata_profile.html', context)




