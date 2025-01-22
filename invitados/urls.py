from django.urls import path
from .views import HomeView, ArticleView, RedesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Nueva ruta para la raíz del sitio
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:article_id>', ArticleView.as_view(), name='article'  ),
    path('redes/', RedesView.as_view(), name='redes')
]
