from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Product, Article


class CategorySerializer(ModelSerializer):
    # Pour filtrer les produits actif on passe par la classe ci-dessous
    products = SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "date_created", "date_updated", "products"]

    def get_products(self, instance):
        # instance est l'instance de la catégorie
        # Si c'est une liste, méthode appelée autant de fois qu'il y a d'entités
        queryset = instance.products.filter(active=True)
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "date_created", "date_updated", "name", "category"]


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        exclude = ["active"]
