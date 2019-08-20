from django.db import models


class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"Name: {self.name}"


class File(models.Model):
    service = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE,
                                default=0, related_name='files')
    file = models.FileField(upload_to='Service/', blank=True)

    def __str__(self):
        return f"Name: {self.file.name}"

