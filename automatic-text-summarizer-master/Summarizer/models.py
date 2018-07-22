from django.db import models
from .validators import validate_file_extension

# Create your models here.
class getFile(models.Model):
    user = models.CharField(max_length=50, default="")
    file = models.FileField(validators=[validate_file_extension])
    length = models.IntegerField()

    def __str__(self):
        return str(self.file)