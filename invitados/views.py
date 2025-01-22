from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from dev_admin.models import ArticleModel


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        articles =ArticleModel.objects.all()
        return render(request, 'home.html', {'articles': articles})
    
class ArticleView(View):
    def get(self, request,article_id, *args, **kwargs):
        article = get_object_or_404(ArticleModel, id = article_id)
        return render(request, 'article.html', {'article': article})
    

class RedesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'redes.html')