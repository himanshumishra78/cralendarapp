from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from django.urls import reverse_lazy


# app_name = 'account'

urlpatterns = [

path('login/',auth_views.LoginView.as_view(),name='login'),
path('logout/',auth_views.LogoutView.as_view(),name='logout'),
# reset password urls
path('password_reset/',
     auth_views.PasswordResetView.as_view(),
     name='password_reset'),
path('password_reset/done/',
     auth_views.PasswordResetDoneView.as_view(),
     name='password_reset_done'),
path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),
path('reset/done/',
     auth_views.PasswordResetCompleteView.as_view(),
     name='password_reset_complete'),
# change password urls
# path('password_change/',
#      auth_views.PasswordChangeView.as_view(),
#      name='password_change'),
path('password-change/', auth_views.PasswordChangeView.as_view() ,name='password_change'),
path('password_change/done/',
      auth_views.PasswordChangeDoneView.as_view(),
      name='password_change_done'),
path('register/',views.register,name='register'),
path('update_email/',views.update_email,name='update_email'),
# path('register_exclusive/',views.register_exclusive,name='register_exclusive'),
# path('edit/', views.edit, name='edit'),
# path('edit_exclusive/',views.edit_exclusive,name='edit_exclusive'),

]
