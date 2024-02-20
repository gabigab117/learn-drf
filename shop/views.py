from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Category, Product, Article
from .serializers import CategoryDetailSerializer, ProductListSerializer, ArticleSerializer, CategoryListSerializer, \
    ProductDetailSerializer


# ReadOnly pour ne pas autoriser toutes les CRUD
class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    # queryset = ou méthode ci-dessous

    def get_queryset(self):
        return Category.objects.filter(active=True)

    def get_serializer_class(self):
        # retrieve detail
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()


class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get("product_id")
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset
