from django.db import models

class Vehicledata(models.Model):
    id             = models.AutoField(primary_key=True)
    invoice_id     = models.BigIntegerField(null=True)
    company_id     = models.BigIntegerField(null=True)
    customer_id    = models.BigIntegerField(null=True)

    matricula      = models.CharField(max_length=22, null=True)   # matricula
    other_data     = models.CharField(max_length=254, null=True)   # color

    class Meta:
        indexes = [
            models.Index(fields=['invoice_id']),
        ]