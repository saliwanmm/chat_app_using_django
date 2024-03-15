from django.urls import path
from .views import homeView, aboutView, sign_up_View, sign_in_View, logout_View


urlpatterns = [
    path('', homeView, name="home"),
    path("about", aboutView, name="about"),
    path("sign_up", sign_up_View, name="sign_up"),
    path("sign_in", sign_in_View, name="sign_in"),
    path("logout", logout_View, name="logout"),
]