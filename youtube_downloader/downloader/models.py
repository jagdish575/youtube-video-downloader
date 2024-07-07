from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=20, unique=True)
    download_url = models.URLField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title

