from django.db import models


class Video(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to='')

    def __str__(self):
        return self.file_name
