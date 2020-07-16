from django.db import models

# Create your models here.
class Comments(models.Model):
    uname = models.CharField(max_length = 16)
    inp_comment = models.CharField(max_length = 160)
    result = models.CharField(max_length = 8)

    def __str__(self):
        return self.uname
