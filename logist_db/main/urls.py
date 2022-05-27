from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('moderator/', views.login, name='login'),
    path('moder_add/', views.add, name='add'),
    # path('moder_add/', views.add, name='add_city'),
    # path('moder_add/', views.add, name='add_regularity'),
    # path('moder_add/', views.add, name='add_delivery'),
    # path('moder_add/', views.add, name='add_options'),

]
