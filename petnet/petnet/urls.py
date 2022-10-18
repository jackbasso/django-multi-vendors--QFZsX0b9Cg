from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, about

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('', include('store.urls')),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),

]
