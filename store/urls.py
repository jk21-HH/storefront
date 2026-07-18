from django.urls import include, path
from rest_framework_nested import routers
from . import views

# URLConf for playground app

router = routers.DefaultRouter()

router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collections')
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register(
    'reviews', views.ReviewViewSet, basename='product-reviews'
)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
]