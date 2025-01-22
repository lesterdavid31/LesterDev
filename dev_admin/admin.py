from django.contrib import admin

# Register your models here.
from .models import ArticleModel

admin.site.register(ArticleModel)