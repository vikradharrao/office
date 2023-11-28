from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members),
    path('members1/', views.members1),
    path('members2/', views.members2),
    path('members3/', views.members3),
]