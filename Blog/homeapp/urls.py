from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
     path('contact_form', views.contact_form, name='contact_form'),
    path("user_register", views.user_register, name="user_register"),
    path("user_login", views.user_login, name="user_login"),
    path('userlogout',views.userlogout, name="userlogout"),
    path('about', views.about, name='about'),
    path('postcreate', PostCreate.as_view(), name="postcreate"),
    path('postlist',PostList.as_view(), name='postlist'),
    path('<slug:slug>/', views.Postdetail.as_view(), name='post_detail'),

]
