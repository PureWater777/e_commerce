from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
# Products
router.register("products", views.ProductViewSet, basename="products")
products_router = routers.NestedSimpleRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")
products_router.register("images", views.ProductImageViewSet, basename="product-images")
# Collections
router.register("collections", views.CollectionViewSet)
# Cart
router.register("carts", views.CartViewSet)
cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", views.CartItemViewSet, basename="cart-items")
# Customer
router.register("customers", views.CustomerViewSet)
# Orders
router.register("orders", views.OrderViewSet, basename="orders")

urlpatterns = router.urls + products_router.urls + cart_router.urls
