from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User,auth

def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1== password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            else:
                user=User.objects.create_user(first_name=first_name, username=username, password=password1)
                user.save()
                print('User Created')
        else:
            print('Password does not match')
        return redirect('/Home')

    else:
        return render(request,'register.html')