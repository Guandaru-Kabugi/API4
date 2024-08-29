from django.urls import path,include
from .views import BookViewSet,SelectRelated
from rest_framework import routers
router = routers.DefaultRouter()
# router2 = routers.DefaultRouter()
router.register(r'books',BookViewSet)
router.register(r'author',SelectRelated,basename='author-book')

urlpatterns = [
    path('api/', include(router.urls)),
    path('',include(router.urls)),
]
