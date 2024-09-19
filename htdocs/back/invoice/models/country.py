from django.db import models

class Country(models.Model):
    id          = models.AutoField(primary_key=True)
    description = models.CharField(max_length=33, null=True, unique=True)


    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]