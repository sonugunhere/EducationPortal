from django.urls import path
from .import views 


urlpatterns = [
    path('home/',views.Home.as_view(),name = 'home'),
    path('create_student/',views.CreateStudent.as_view(),name = 'create_student'),
    path('student_list/',views.StudentList.as_view(),name = 'student_list'),
    path('student_update/<int:id>/',views.UpdateStudent.as_view(),name='student_update'),
    path('student_delete/<int:id>/',views.StudentDelete.as_view(),name='student_delete'),
    
]
