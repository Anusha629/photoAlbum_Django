from django.urls import path
from . import views 


urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('photo/',views.photo_sharing, name='photo_sharing'),
    path('logout/', views.user_logout, name='logout'),
    

    
    
]

