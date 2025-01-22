from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.http import request
from .models import ArticleModel
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.


class RegisterView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'register.html')

    
    def post(self,request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        passwrod = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso")
            print('El nombre del usuario ya está en uso') 
            return render(request, 'register.html')
        
        superUser = User.objects.create_user(username=username, email=email, password=passwrod)

        login(request, superUser)
        messages.success(request, "Registro Exitoso")
        print('Registro Exitoso')
    
        return redirect('article_list')

class LoginView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self,request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            print('Sesión iniciada')
            return redirect('article_list')  
        else:
            print('Usuario o contraseña incorrectos')
            messages.error(request,'Nonbre del usuario y contraseña incorrectos')
            return render(request, 'login.html')

class logoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        print('Sesión cerrada')
        return redirect('home')



class ListArticleView(LoginRequiredMixin,View):
    def get (self, request, *args, **kwargs):
        articles = ArticleModel.objects.all()
        return render(request, 'list_article.html', {'articles': articles})
    

class CreateArticleView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_article.html')

    def post(self,request,*args, **kwargs):
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')

        new_article = ArticleModel(title=title,content= content, image= image)
        new_article.save()
    
        return redirect('article_list')
    
class EditArticleView(LoginRequiredMixin, View):

    def get(self, request, article_id,*args, **kwargs):
        article = get_object_or_404(ArticleModel,id =article_id)
        return render(request, 'edit_article.html', {'article':article})
    
    def post(self,request,article_id, *args, **kwargs):
        article = get_object_or_404(ArticleModel, id = article_id)

        article.title = request.POST['title']
        article.content = request.POST['content']
        article.image = request.FILES.get('image')
        article.save()

        return redirect('article_list')

class DeleteArticleView(View):
    def post(self,request,article_id, *args, **kwargs):
        article = get_object_or_404(ArticleModel, id = article_id)
        article.delete()
        return redirect('article_list')