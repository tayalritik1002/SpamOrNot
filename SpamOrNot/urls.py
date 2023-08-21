"""
URL configuration for SpamOrNot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import home, Login,register,addcontact,searchbyname,search,searchbyphone
#  mark_spam, search_by_name, search_by_phone, view_person_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', register, name="register"),
    path('', Login, name="login"),
    path('home/', home, name='home'),
    path('addcontact/',addcontact,name="addcontact"),
    path('search', search, name='search'),
    path('searchbyname', searchbyname,name='searchbyname'),
    path('searchbyphone', searchbyphone,name='searchbyphone'),
    # path('api/person/<int:person_id>', view_person_details),
]

