from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator
from django.db import models
from Portfolio.settings import LOGS_LIMIT


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
    path_validator = RegexValidator(regex=r'^\/[(\w|\d)*\/]+$',
                                    message='The path is incorrect. Example: /api/ict/unit/')
    path = models.CharField(validators=[], max_length=100)
    is_ajax = models.BooleanField()
    is_secure = models.BooleanField()

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        return f'Log(datetime={self.datetime}, status_code={self.status_code}, path={self.path})'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        Overriding the save method in order to limit the amount of Logs that can be saved in the database.
        The limit is LOGS_LIMIT, after that the first ones inserted will be eliminated
        """
        count = Logs.objects.all().count()
        super().save()
        if count >= LOGS_LIMIT:
            Logs.objects.first().delete()


class Project(models.Model):
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
    description = models.TextField()
    website = models.URLField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    subtitle = models.CharField(max_length=30)
    categories = models.ManyToManyField('ProjectCategory')

    def __str__(self):
        return f"Name: {self.name}, Link: {self.website}"


class ProjectCategory(models.Model):
    name = models.SlugField(primary_key=True)

    def __str__(self):
        return f"ProjectCategory(name={self.name})"


class Gallery(models.Model):
    """
    a photo that will reference a project
    (many photos will reference a single project)
    """
    photo = models.ImageField(upload_to='Gallery', default="Kalwak.svg")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0, related_name='images')

    def __str__(self):
        return f"Name: {self.photo.name}"

    class Meta:
        verbose_name_plural = "Galleries"
