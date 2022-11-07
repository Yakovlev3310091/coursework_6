from django.urls import include, path

# TODO настройка роутов для модели
from rest_framework.routers import SimpleRouter

from skymarket.ads.views import CommentViewSet, AdViewSet

router_ad = SimpleRouter()
router_ad.register("ads", AdViewSet)

urlpatterns = [
    path("", include(router_ad.urls)),
    path("ads/<int:ad_id>/comments/", CommentViewSet.as_view({"get": "list", "post": 'create'})),
    path("ads/<int:ad_id>/comments/<int:id>/", CommentViewSet.as_view({'get': 'retrieve',
                                                                       'put': 'update',
                                                                       'patch': 'partial_update',
                                                                       'delete': 'destroy'})),

]
