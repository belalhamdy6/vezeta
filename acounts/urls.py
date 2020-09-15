from django.urls import path
from . import views

app_name = 'acounts'
urlpatterns = [

    path('doctors/', views.doctor_lists, name='doctor_list'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('updata_profile/', views.updata_profile, name='updata_profile'),
    path('<slug:slug>/', views.doctors_detail, name='doctor_detail'),

]