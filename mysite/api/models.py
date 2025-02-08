from django.db import models

# Create your models here.
class BlogPost(models.Model):
    Question = models.TextField()
    Answer = models.TextField()
    published_time_stamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title