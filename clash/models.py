from django.db import models

def img(instance, filename):
    return f"{instance.nivel}-{filename}"

class heroes(models.Model):
    nivel =models.CharField(primary_key=True, max_length=1000)
    image =models.ImageField(upload_to=img, blank=True, null=True)0
