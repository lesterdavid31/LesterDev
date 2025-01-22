from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class ArticleModel(models.Model):
    title = models.CharField(max_length=50)
    content = CKEditor5Field('text', config_name='extends',null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/',null=True, blank=True)  # Define la carpeta 'articles'

    def __str__(self) -> str:
        return self.title
    
    
