from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted', views.restricted),
    path('detail/<str:id>', views.user_detail, name="user_detail"),
    path('ops/<str:id>', views.user_ops, name="user_ops")
]
