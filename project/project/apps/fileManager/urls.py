from django.urls import path
from . import views

app_name = 'fileManager'

urlpatterns = [
    path('video', views.GetVideoTemplate.as_view(), name='video'),
    path('getVideo/<int:id>', views.Getvideo.as_view(), name='get_video'),
    path('getAssignment/<int:id>', views.GetAssignment.as_view(), name='getAssignment'),
    path('getAnswer/<int:id>', views.GetAnswer.as_view(), name='getAnswer'),
    path('getProfileImage/<int:id>', views.GetProfilePicture.as_view(), name='getProfileImage'),

]
