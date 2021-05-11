from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change_password/', views.PasswordChangeView
         .as_view(template_name="./passwordForms/changePassword.html"),
         name="change_password"
         ),

    path('reset_password/',
         auth_views.PasswordResetView
         .as_view(template_name="./passwordForms/resetPassword.html"),
         name="reset_password"
         ),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView
         .as_view(template_name="./passwordForms/password_reset_sent.html"),
         name="password_reset_done"
         ),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView
         .as_view(template_name="./passwordForms/password_reset_form.html"),
         name="password_reset_confirm"
         ),

    path('reset/done/',
         auth_views.PasswordResetCompleteView
         .as_view(template_name="./passwordForms/password_reset_done.html"),
         name="password_reset_complete"
         )
]
