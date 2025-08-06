# from django.urls import path
# from . import views

# # urlpatterns = [
# #     path('chat/', views.index, name='index'),
# #     path('chat/<str:room_name>/', views.room, name='room'),
# #     path('stream_webhook/', views.stream_webhook, name='stream_webhook'),
# # ]
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]