from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class NewsPost(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(max_length=3)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID:{self.id} - {self.title} - {self.link}'


class Comment(models.Model):
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField(max_length=2550)
    creation_date = models.DateTimeField(auto_now_add=True)
    news_post_comment = models.ForeignKey('NewsPost', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.author_name} - {self.content[:50]} - {self.creation_date}'
