from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('/',views.index,name='index_typing'),
    path('history/',views.history,name='history'),
    path('display/',views.display,name='display'),
]
