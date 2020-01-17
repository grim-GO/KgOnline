from django.db import models
import datetime
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField("название поста", max_length=200)
    post_text = models.TextField("текст поста")
    pub_date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class User(models.Model):
    user_name = models.CharField("имя пользователя", max_length=50)
    quantity_post = models.CharField("количество постов", max_length=20)
    register_date = models.DateTimeField("дата регистрации")


class Comment(models.Model):
    author_name = models.CharField("имя пользователя", max_length=50)
    comment_text = models.CharField("название поста", max_length=200)
    comment_date = models.DateTimeField("дата комментирования")

