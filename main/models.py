from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    icon = models.CharField(max_length=50, default="fas fa-globe")

    def __str__(self):
        return self.name