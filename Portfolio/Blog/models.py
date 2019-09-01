from django.db import models


class Blog(models.Model):
    title = models.CharField(blank=False, max_length=100)
    author = models.CharField(blank=False, max_length=100)
    tags_options = [("Development", "Development"), ("Social", "Social Media"),
                    ("Startup", "Startup"), ("Security", "Security"),
                    ("Design", "Graphic Design")]
    tag = models.CharField(choices=tags_options, max_length=10)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=False, max_length=20000)
