from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
# Products
router.register("products", views.ProductViewSet, basename="products-detail")
products_router = routers.NestedSimpleRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")
# Collections
router.register("collections", views.CollectionViewSet)

urlpatterns = router.urls + products_router.urls
