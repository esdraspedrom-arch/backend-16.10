from django.contrib import admin
from django.contrib.admin import views
from django.urls import path
from ALPHA.views import home, segundapgn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('segunda/', views.segundapgn, name='segundapgn'),
]
