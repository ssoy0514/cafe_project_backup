"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from ..backend import views
# from rest_framework import urls
# # from knox import views as knox_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('consumsers/', include('consumers.urls')),
#     # path('store/',include('store.urls')),
#     # path('main/', include('main.urls')),
#     # path("profile_all/", include("profile_all.urls")),
#     # path("profile_all/auth/", include("knox.urls")),
#     # path('profile_all/auth/logout',knox_views.LogoutView.as_view(), name="knox-logout"),
#     path('signup/', views.UserCreate.as_view()),
#     path('api-auth/', include('rest_framework.urls'))
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('profile.urls')),
    ]