from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('moderator/', views.login, name='login'),
    path('moder_create/', views.add, name='add'),
    path('moder_edit/', views.edit, name='edit'),
    path('moder_delete/', views.delete, name='delete'),
]
