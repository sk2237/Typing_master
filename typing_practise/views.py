from django.shortcuts import render,get_object_or_404
from .models import Typing_practise
# Create your views here.
def index(request):
  return render(request,'typing_practise/index.html')

def history(request):
  if request.method == 'POST':
    user_id = request.POST['user_id']
    typing_speed = request.POST['typing_speed']
    accuracy = request.POST['typing_accuracy']

    typing_practise = Typing_practise(user_id=user_id,typing_speed=typing_speed,accuracy=accuracy)
    typing_practise.save()

    user_data = Typing_practise.objects.filter(user_id=user_id)
  return render(request,'typing_practise/dashboard.html',{'user_data':user_data})

def display(request):
  user_id = request.POST['user_id']
  user_data = Typing_practise.objects.filter(user_id=user_id)
  return render(request,'typing_practise/dashboard.html',{'user_data':user_data})
