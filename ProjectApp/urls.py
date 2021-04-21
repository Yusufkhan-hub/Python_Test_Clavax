from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('add-details',views.add_student_details,name="add-details"),
    path('edit-details/<int:pk>/',views.edit_student_details,name="edit-details"),
    path('register-admin',views.register_admin,name='register-admin'),

]
