from django.urls import path
from . import views
urlpatterns = [
    path('<int:short>',views.bitly,name="bitly"),
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('create',views.create,name="create"),
]
