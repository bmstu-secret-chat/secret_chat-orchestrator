from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chats/', include('backend.urls')),
    path('api/messages/', include('realtime.urls')),
]
