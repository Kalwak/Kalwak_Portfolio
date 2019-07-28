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
