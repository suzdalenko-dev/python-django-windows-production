from django.db import models

class Document(models.Model):
    id          = models.AutoField(primary_key=True)
    description = models.CharField(max_length=41, null=True)
    value       = models.PositiveIntegerField(default=0)
    ejercicio   = models.CharField(max_length=7, null=True)

    company_id  = models.BigIntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['description']),
            models.Index(fields=['company_id']),
            models.Index(fields=['ejercicio']),
        ]