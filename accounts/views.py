from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

# Create your views here.
def index(request):
  return render(request,'accounts/index.html')

def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.error(request, 'That Email is taken')
        return redirect('register')
      else:
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        messages.success(request,":You are now registered")
        return redirect('index')
    else:
      messages.error(request,'passwords do not match')
      return redirect('register')
  else:
    return render(request,'accounts/register.html')
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user =auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      messages.success(request,'You are logged in')
      return redirect('index_typing')
    else:
      messages.error('Invalid Credentials')
      return redirect('login')
  else:
    return render(request,'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'Logout successful')
    return redirect('index')
