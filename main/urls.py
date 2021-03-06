from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),

    path('group/<str:name>/<str:code>/', views.group , name='group'),
    
    path('spec/<int:id>', views.spec, name='spec'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('my_subjects', views.my_subjects, name='my_subjects'),
    path('result/<str:code>', views.result, name='result'),

    path("result/<str:code>/change/",views.change_student,name="change-student"),
    path('studentinfo/<str:name>/<int:id>' ,views.studentinfo, name = 'studentinfo'),
]
