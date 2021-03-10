from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reminder/', views.reminder, name='reminder'),
]