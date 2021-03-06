from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resource, name='resources'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='detail'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('newresource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]