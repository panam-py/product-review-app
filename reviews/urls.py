from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ImageViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = router.urls
# urlpatterns.append(path('image', ImageViewSet.as_view()))