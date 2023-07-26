from django.urls import path
from . import views
urlpatterns = [
    path("<int:id>", views.doctor_interface, name="doctor")
]
