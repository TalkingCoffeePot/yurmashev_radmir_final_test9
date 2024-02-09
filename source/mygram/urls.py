"""
URL configuration for mygram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from feed.views import FeedView, post_like_view, PostDetailedView, SearchResultsView
from accounts.views import UserRegisterView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', FeedView.as_view(), name='feed'),
    path('sign_up/', UserRegisterView.as_view()),
    path('feed/<int:post_pk>/', PostDetailedView.as_view(), name='feed_post'),
    path('search_result/', SearchResultsView.as_view(), name='search_results'),
    path('likes/', post_like_view, name='post_likes'),
    path('api/', include('api_v1.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
