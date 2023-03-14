from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('sign/',views.sign,name='sign'),
    path('logout/',views.logout,name='logout'),

]
