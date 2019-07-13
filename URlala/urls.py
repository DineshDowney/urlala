from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^$',views.home,name='random'),
    path('admin/', admin.site.urls),
]
