from django.db import models


class Blog(models.Model):
    title = models.CharField(blank=False, max_length=100)
    author = models.CharField(blank=False, max_length=100)
    tags_options = [("development", "Development"), ("social", "Social Media"),
                    ("startup", "Startup"), ("security", "Security"),
                    ("design", "Graphic Design")]
    tag = models.CharField(choices=tags_options, max_length=11)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(blank=False, max_length=30000)
