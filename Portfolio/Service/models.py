from django.core.validators import RegexValidator
from django.db import models


class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    description = models.TextField(max_length=1000)
    telephone_validator = RegexValidator(regex=r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$", message="Telephone "
                                                                                                        "format is "
                                                                                                        "incorrect",
                                         code='invalid_telephone')
    telephone = models.CharField(max_length=30, validators=[telephone_validator])

    def __str__(self):
        return f"Name: {self.name}"


class File(models.Model):
    service = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE,
                                default=0, related_name='files')
    file = models.FileField(upload_to='Service/', blank=True)

    def __str__(self):
        return f"Name: {self.file.name}"

    def delete(self, *args, **kwargs):
        storage, path = self.file.storage, self.file.path
        super(File, self).delete(*args, **kwargs)
        storage.delete(path)


class Service(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE,
                                        default=0, related_name='services')
    service = models.CharField(max_length=100)

    def __str__(self):
        return f"Service{self.service}"
