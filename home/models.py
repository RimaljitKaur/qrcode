from django.db import models

# Create your models here.

class Code(models.Model):
    qr_code = models.ImageField(upload_to='images/')
    qr_name = models.CharField(max_length=50)