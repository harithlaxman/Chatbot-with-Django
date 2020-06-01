from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('refresh/<str:user_name>', views.refresh, name='refresh'),
    path('del_request/<str:user_name>', views.del_request, name='del_request'),
]
