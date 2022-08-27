from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def signupp(request):
    if request.method=='POST':

        username = request.POST['username']
        password = request.POST['password1']
        password1 = request.POST['password2']

        if password1 == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return render(request,'signupp.html')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.info(request, 'User Created')
                return redirect('loginn')
        else:
            messages.info(request, 'password not match')
            return render(request,'signupp.html')
    else:    
        return render(request,'signupp.html')

def loginn(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('afterlog') 
        else:
            messages.info(request,'invalid credentials')
            return redirect('loginn')
    else:
        return render(request,'loginn.html')

def afterlog(request):
    return render(request,'afterlog.html')