from django.contrib import admin
from django.urls import path
from dogscup import views
from django.conf.urls import include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.Home),
    path('dogscup/',include('dogscup.urls')),
]