from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator
from django.db import models


class Logs(models.Model):
    """
    Saving data to this model about every request
    """
    datetime = models.DateTimeField(auto_now=True)
    status_code = models.PositiveSmallIntegerField()
    status_text = models.TextField()
    response = JSONField()
    request = JSONField()
    ipv4_address = models.GenericIPAddressField()
    path_validator = RegexValidator(regex='^\/[(\w|\d)*\/]+$',
                                    message='The path is incorrect. Example: /api/ict/unit/')
    path = models.CharField(validators=[], max_length=100)
    is_ajax = models.BooleanField()
    is_secure = models.BooleanField()

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        return f'Log(datetime={self.datetime}, status_code={self.status_code}, path={self.path})'


class Proyect(models.Model):
    """
    model that will give information
    about the different projects that
    we have worked on, a link if it
    is a web page or, alternatively,
    an executable
    """
    name = models.CharField(max_length=100)
    cover_page = models.ImageField(upload_to='cover_pages',
                                   default="Kalwak.svg")
    description = models.CharField(max_length=1000)
    website = models.URLField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"Name: {self.name}, Link: {self.website}"


class Gallery(models.Model):
    """
    a photo that will reference a project
    (many photos will reference a single project)
    """
    photo = models.ImageField(upload_to='Gallery', default="Kalwak.svg")
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"Name: {self.photo.name}"
