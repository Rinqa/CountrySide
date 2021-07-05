"""CountrySide URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home.views import UserRegister, shtetet_search, shtetet_info, homepage,Addinfo, shtetet_flags,like,dislike,sorting,approve_info,unapproved_info,dissapprove_info
from django.contrib.auth import views as userViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', UserRegister, name='sign-up'),
    path('login/', userViews.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', userViews.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('shtetet_search/', shtetet_search, name="shtetet-search"),
    path('shtetet_info/<int:pk>/', shtetet_info, name="shtetet-info"),
    path('unapprove/', unapproved_info, name="unapproved"),
    path('shtetet_info_approve/<int:pk>/', approve_info, name="shtetet-info-approve"),
    path('shtetet_info_dissapprove/<int:pk>/', dissapprove_info, name="shtetet-info-dissapprove"),
    path('shkruaj/<int:shteti>/', Addinfo, name="shto"),
    path('shkruaj/', Addinfo, name="shto"),
    path('kontinentet/<int:pk>/', shtetet_flags, name="shtetet"),
    path('kontinentet-sort/<int:pk>/', sorting, name="shtetet_sorted"),
    path('like/<int:pk>/', like, name="likes"), 
    path('dislike/<int:pk>/', dislike, name="dislikes"),
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
