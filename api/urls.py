from django.urls import path
from .import views

urlpatterns = [
    path("", views.plate_list, name="plates"),
    path("detail/<str:pk>/", views.plate_detail, name="detail"),
    path("create/", views.plate_create, name="create"),
    path("update/<str:pk>/", views.plate_update, name="update"),
    path("delete/<str:pk>/", views.plate_delete, name="delete"),
]
