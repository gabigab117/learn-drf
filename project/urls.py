from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.views import CategoryViewset, ProductViewset, ArticleViewset, AdminCategoryViewset, AdminArticleViewset


router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename="category")
router.register('product', ProductViewset, basename="product")
router.register('article', ArticleViewset, basename="article")
router.register('admin/category', AdminCategoryViewset, basename="admin-category")
router.register('admin/articles', AdminArticleViewset, basename="admin-articles")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]


# Router : permet de définir auto toutes les url accessibles pour un endpoint.
