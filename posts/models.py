from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    link = models.CharField(max_length=256, unique=True)
    creation_date = models.DateField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True, null=True)

    author_name = models.CharField(max_length=256)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
