from django.urls import path
from .views import ListArticleView, CreateArticleView, EditArticleView, DeleteArticleView, RegisterView, LoginView, logoutView


urlpatterns = [
    path('article_list', ListArticleView.as_view(), name='article_list' ),
    path('create_article', CreateArticleView.as_view(), name='create_article'),
    path('edit_article/<int:article_id>/',EditArticleView.as_view(), name='edit_article'),
    path('delete_article/<int:article_id>/', DeleteArticleView.as_view(), name='delete_article'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout')
    
]


