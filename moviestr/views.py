from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def index(request):
    return render(request,'index.html')

def playlist(request):
    return render(request,'playlist.html')
# def loginn(request):
#     return render(request,'loginn.html')

# def signupp(request):
#     return render(request,'signupp.html')