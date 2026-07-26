from django.urls import include, path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register(
    'reviews', views.ReviewViewSet, basename='product-reviews'
)

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register(
  'items', views.CartItemViewSet, basename='cart-items'
)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
    path(r'', include(cart_router.urls)),
]