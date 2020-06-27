from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    url = models.URLField()
    category = models.CharField(max_length=100)
    subcategory = models.TextField(max_length=50)
    author = models.TextField(max_length=50)

    def rating_average(self):
        sum = 0
        ratings = Rating.objects.filter(video=self)

        if len(ratings) > 0:

            for rating in ratings:
                sum += rating.stars

            return sum / len(ratings)
        else:
            return 0

    def comments_list(self):

        comments = Rating.objects.filter(video=self)
        comments_list = []

        for i in comments:
            comments_list.append(i.comments)
        return comments_list


class Rating(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    class Meta:
        unique_together = (('user', 'video'),)
        index_together = (('user', 'video'),)
