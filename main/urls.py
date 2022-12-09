from rest_framework import routers
from django.urls import path, include

from .views import CategoryListViewSet, CategoryDetailViewSet, UserListView, UserDetailView, ClothesListViewSet

app_name = 'main'

router = routers.DefaultRouter()

router.register(r'category-list', CategoryListViewSet, basename='category-list')
router.register(r'category-detail', CategoryDetailViewSet, basename='category-detail')
router.register(r'clothes-list', ClothesListViewSet, basename='clothes-list')


urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
