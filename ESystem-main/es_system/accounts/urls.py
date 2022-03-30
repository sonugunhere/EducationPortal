from django.urls import path, include
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [ 
    
    path("",views.Index.as_view(),name="index"),
    path("login/",views.Login.as_view(),name="login"),
    path("student_register/",views.StudentRegister.as_view(),name="student_register"),
    path("user_dashboard/",views.UserDashboard.as_view(),name="user_dashboard"),
    path("school_registrations/",views.SchoolRegistration.as_view(),name="school_registrations"),
    path("school_logout/",views.SchoolLogout.as_view(),name="school_logout"),



    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),

]
