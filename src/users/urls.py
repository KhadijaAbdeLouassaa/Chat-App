from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
# create your urls here.
app_name = "users"

urlpatterns = [
	
    path('signup/', views.SignupView.as_view(), name = 'signup' ),
    path('login/', LoginView.as_view(template_name = "users/login.html"), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    
    path('profile/', views.edit_profile, name = 'profile')
]