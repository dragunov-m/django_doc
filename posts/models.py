from datetime import datetime
from django.db import models


# One - to - one
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now())
    slug = models.CharField(max_length=240, null=True, blank=False)
    title = models.CharField(default='default title', max_length=20)
    post = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now())
    comment = models.TextField()

    def __str__(self):
        return self.comment
