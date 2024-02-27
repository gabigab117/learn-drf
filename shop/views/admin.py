from rest_framework.viewsets import ModelViewSet
from shop.serializers import CategoryDetailSerializer, CategoryListSerializer, ArticleSerializer
from shop.models import Category, Article
from shop.permissions import IsAdminAuthenticated


# On va utiliser un ModelViewset car les admins peuvent tout voir


class AdminCategoryViewset(ModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        # retrieve detail
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()


class AdminArticleViewset(ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()
