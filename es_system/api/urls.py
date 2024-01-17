from django.urls import path
from .import views


urlpatterns=[
    
    path('',views.StudentList.as_view(),name = 'studentlist'),
    path('studentdetail/<int:pk>/',views.StudentDetail.as_view(),name = 'studentdetail'),
    
    
]