from django.conf.urls import url
from django.urls import path
from myApp_1 import views

app_name = "myApp_1"

urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/',views.MusicianDetail.as_view(),name='musician_details'),
    path('add_musician/',views.AddMusician.as_view(),name='add_musician'),
    path('musician_update/<pk>/',views.UpdateMusician.as_view(),name='musician_update'),
    path('delete_musician/<pk>/',views.DeleteMusician.as_view(),name='delete_musician'),

 ]
