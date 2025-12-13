from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.ProfileViewSet,basename='profile')
router.register('feed',views.ProfileFeedViewSet,basename='feed')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('', include(router.urls))
]