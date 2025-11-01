from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer
from .permissions import IsAdminUser, IsSellerUser, IsCustomerUser

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] # Anyone can view a user's products

    def get_queryset(self):
        user_pk = self.kwargs['user_pk']
        return Product.objects.filter(seller__pk=user_pk)

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS: # GET, HEAD, OPTIONS
            self.permission_classes = [permissions.AllowAny]
        else: # POST
            self.permission_classes = [permissions.IsAuthenticated, IsSellerUser | IsAdminUser]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        # All users (including authenticated sellers, customers, and unauthenticated users) should see all products
        return Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsSellerUser | IsAdminUser | IsCustomerUser]

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS: # GET, HEAD, OPTIONS
            self.permission_classes = [permissions.AllowAny] # Allow any user to view product details
        else: # PUT, PATCH, DELETE
            self.permission_classes = [permissions.IsAuthenticated, IsSellerUser | IsAdminUser]
        return [permission() for permission in self.permission_classes]
