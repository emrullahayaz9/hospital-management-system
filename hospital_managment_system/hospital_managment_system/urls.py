
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("index.urls")),
    path('auth/', include("x.urls")),
    path('admin/', admin.site.urls),
    path('doctor/', include("doctor_interface.urls")),
]
