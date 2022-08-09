from django.shortcuts import render

from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer