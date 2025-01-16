
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  #this is for the home page
    path('about/', include('about.urls')),
    path('shop/', include('shop.urls')),
    
    
] 
