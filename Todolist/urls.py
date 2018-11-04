from django.contrib import admin
from django.urls import path, include
from toDoListSite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('toDoListSite.toDoListUrls'))
]
