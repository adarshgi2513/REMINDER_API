from django.urls import path
from . import views
from .views import ReminderAPIView,DataList

urlpatterns = [
    path('', views.index, name='index'),
     path('create/', ReminderAPIView.as_view(), name='create-reminder'),
     path('listdata/',DataList.as_view(),name="data-list"),

    
       

]