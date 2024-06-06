from django.contrib import admin
from django.urls import path
from quizapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('show/', show, name="show"),
    path('logout/', logout, name="logout"),
    path('delete/<id>', delete, name="delete"),
    path('edit/<id>', edit, name= "edit"),
]



