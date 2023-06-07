from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_img/')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    body = models.TextField()

    def __str__(self):
        return self.title
