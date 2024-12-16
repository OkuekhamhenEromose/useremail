
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('useremailapps/', admin.site.urls),
    path('api/', include('useremailapps.urls')),
]
