from django.contrib import admin
from django.urls import path
from solar.views import calculo_solar

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', calculo_solar),
]
