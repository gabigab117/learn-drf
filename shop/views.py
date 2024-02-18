from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Category, Product, Article
from .serializers import CategorySerializer, ProductSerializer, ArticleSerializer


# ReadOnly pour ne pas autoriser toutes les CRUD
class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    # queryset = ou méthode ci-dessous

    def get_queryset(self):
        return Category.objects.filter(active=True)


class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ArticleViewset(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get("product_id")
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset
