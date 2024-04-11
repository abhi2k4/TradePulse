
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('crypto/', views.crypto, name='crypto'),
    path('news/', views.news, name='news'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('login/', views.login, name='login'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)