from django.urls import path, include
from .views import *

urlpatterns = [
    path('', EgeTaskHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<int:cat_id>/', EgeTaskCategory.as_view(), name='category'),
    path("tasks/<slug:number_task>/", show_task, name='task'),
]
