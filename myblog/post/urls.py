from django.urls import path
from . import views

urlpatterns = [
    path('', views.post),
    path('post/<str:pk>', views.page)
]