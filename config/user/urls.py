from django.urls import path, include

from .views import check_token, profile_view

urlpatterns = [
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('check_token/', check_token),
    path('profile/', profile_view)
]