from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.gender_index),
    path('gender/create', views.gender_create),
    path('gender_store', views.gender_store),
    path('gender/view/<int:id>', views.gender_show),
    path('gender/edit/<int:id>', views.gender_edit),
    path('gender_update/<int:id>', views.gender_update),
    path('gender/delete/<int:id>', views.gender_delete),
    path('gender_destroy/<int:id>', views.gender_destroy),
    path('users', views.user_index),
    path('user/create', views.user_create),
    path('user_store', views.user_store),
]
