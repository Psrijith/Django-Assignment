from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
 
def HomePage(request):
    return render(request, 'initial.html')
 
def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render(request, 'initial.html')
        else:
            return HttpResponse("User not found or Incorrect , Please Sign Up!")

    return render(request, 'login.html')

def SignupPage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!! Retry")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def TutorHome(request):
    return render(request, 'tutorhome.html')

def AdminHome(request):
    return render(request, 'adminhome.html')

def StudentHome(request):
    return render(request, 'studenthome.html')
