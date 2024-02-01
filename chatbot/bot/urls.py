from django.urls import path
from . import views
from django.contrib.auth import views as v


urlpatterns=[
    path('',views.home,name='home'),
    path('login/',v.LoginView.as_view(template_name='bot/login.html'),name='login'),
    path('logout/',views.logoutPage,name='logout')
]