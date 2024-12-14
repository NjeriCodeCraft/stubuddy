from django.shortcuts import render, redirect
from .models import NavbarItem, StudyTip, Course
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse


def sign_up(request):
    if request.method == 'POST':
        agent=sign_up(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        agent.save()
        return redirect('/sign-up')
    else:
        return render(request,'sign-up.html')
   

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Log the user in
                login(request, user)
                # Redirect to the dashboard after login
                return redirect('dashboard')
            else:
                # Return an error if authentication fails
                return HttpResponse("Invalid login details")
    else:
        form = AuthenticationForm()

    return render(request, 'sign-in.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def study_schedule(request):
    return render(request, 'study-schedule.html')

def rtl(request):
    return render(request, 'rtl.html')

def study_buddy(request):
    return render(request, 'study-buddy.html')

def virtual_reality(request):
    return render(request, 'virtual-reality.html')

def base_context(request):
    navbar_items = NavbarItem.objects.filter(is_active=True)
    return {'navbar_items': navbar_items}

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('sign-in')

def study_schedule(request):
    study_tips = StudyTip.objects.all()  # Fetch all the study tips
    return render(request, 'study-schedule.html', {'study_tips': study_tips})


def study_schedule(request):
    courses = Course.objects.all()  # Fetch all courses
    return render(request, 'study-schedule.html', {'courses': courses})





def sign_out(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('sign-in')
