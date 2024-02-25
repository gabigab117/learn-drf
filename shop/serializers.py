from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Product, Article


class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "date_created", "date_updated", "description"]

    def validate_name(self, value):
        # Autant faire un unique=True dans lel modèle, mais bon c'est pour le fun
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("La catégorie existe déjà")
        return value

    def validate(self, data):
        if data['name'] not in data["description"]:
            raise serializers.ValidationError("Le nom doit être dans la description")
        return data


class CategoryDetailSerializer(ModelSerializer):
    # Pour filtrer les produits actif on passe par la classe ci-dessous
    products = SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "date_created", "date_updated", "products"]

    def get_products(self, instance):
        # instance est l'instance de la catégorie
        # Si c'est une liste, méthode appelée autant de fois qu'il y a d'entités
        queryset = instance.products.filter(active=True)
        serializer = ProductListSerializer(queryset, many=True)
        return serializer.data


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "date_created", "date_updated", "name", "category", "ecoscore"]


class ProductDetailSerializer(ModelSerializer):
    articles = SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "date_created", "date_updated", "name", "category", "articles"]

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ["name", "description", "active", "price", "product"]

    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError("Le prix doit être supérieur à 1e")
        return value

    def validate(self, data):
        if not data["product"].active:
            raise serializers.ValidationError("Le produit doit être actif")
        return data
