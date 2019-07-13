from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^$',views.home,name='random'),
    path("<str:token>",views.create_url,name="name2"),
    path('admin/', admin.site.urls),
]
