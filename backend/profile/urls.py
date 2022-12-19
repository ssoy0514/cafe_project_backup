# from django.urls import path, include
# from main import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# # router.register(r"menu", views.MenuViewSet)




# urlpatterns = [
#     # path('', include(router.urls)),
#     # path('api/',include('rest_framework', namespace="rest_framework")),
# ]

# from django.urls import path, include
# from .views import HelloAPI, RegistrationAPI, LoginAPI

# urlpatterns = [
#     path("hello/", HelloAPI),
#     path("auth/register/", RegistrationAPI.as_view()),
#     path("auth/login/", LoginAPI.as_view()),
#     # path("auth/user/", UserAPI.as_view()),
# ]
from django.urls import path, include
from . import views
from rest_framework import urls
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns =[
    path('profile/', views.ProfileCreate.as_view()),
    path('profile/consumer', views.ConsumerCreate.as_view()),
    path('profile/store', views.StoreCreate.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
    # 일반 회원 회원가입/로그인
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('user/password/reset/', PasswordResetView.as_view(),name='rest_password_reset'),
    path('user/password/reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    ]