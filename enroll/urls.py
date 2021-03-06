from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.sign_up,name="sign"),
    path('login/',views. user_login,name="login"),
    path('profile/', views.Profile, name="profile"),
    path('logout/', views.Logout, name='logout'),
    path('change1', views.user_change1, name='change1')
]
