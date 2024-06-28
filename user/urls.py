from django.urls import path
from django.contrib.auth import views as dj_view
from chatit import settings
from .import views

app_name="user"
urlpatterns = [
    path('signup/', views.sign_up , name='signup'),
    path('login/', dj_view.LoginView.as_view(template_name='user/login.html') , name='login'),
    path('logout/', dj_view.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL) , name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    
]