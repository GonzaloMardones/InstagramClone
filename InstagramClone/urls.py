"""Instagramclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
Este es el doctype de Django donde alojo las url de platsigram
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

	path('admin/',admin.site.urls),
	
	#path('hello-world/',local_views.hello_world, name='hello_world'),
	#path('sorted/',local_views.sort_integers,name='sort'),
	#path('hi/<str:name>/<int:age>/', local_views.say_hi, name='hi'),

    path('',include(('posts.urls','posts'), namespace='posts')),
    path('users/',include(('users.urls','users'), namespace='users')),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
"""
una vista en django es una funcion
"""
