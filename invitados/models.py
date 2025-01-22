from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title