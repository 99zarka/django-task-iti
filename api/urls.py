from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, LoginView, UserListView, UserProductListView, ProductListCreateView, ProductDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/<int:user_pk>/products/', UserProductListView.as_view(), name='user-products'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
