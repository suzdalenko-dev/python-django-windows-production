from django.db import models

class Article(models.Model):
    id          = models.AutoField(primary_key=True)
    company_id  = models.BigIntegerField(null=True)

    artcode     = models.PositiveBigIntegerField(default=0)
    description = models.CharField(max_length=254, null=True)
    price       = models.DecimalField(max_digits=11, null=True, decimal_places=2)
    iva         = models.DecimalField(max_digits=11, null=True, decimal_places=2)
    ivatype     = models.CharField(max_length=11, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['company_id']),
            models.Index(fields=['description']),
        ]