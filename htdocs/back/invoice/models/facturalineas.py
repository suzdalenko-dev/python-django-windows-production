from django.db import models

class Facturalineas(models.Model):
    id           = models.AutoField(primary_key=True)
    invoice_id   = models.BigIntegerField(null=True)
    company_id   = models.BigIntegerField(null=True)
    serie        =  models.CharField(max_length=22, null=True)

    article_id    = models.BigIntegerField(null=True)
    article_num   = models.BigIntegerField(null=True)
    article_name  = models.CharField(max_length=254, null=True)

    cantidad      = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    precio        = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    importe_bruto = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    
    descuento     = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    descuento_val = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    importe_con_descuento = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    iva_porcent  = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    iva_valor    = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    importe_res  = models.DecimalField(max_digits=11, decimal_places=2, null=True)

    iva_type     = models.CharField(max_length=11, null=True)

    

    class Meta:
        indexes = [
            models.Index(fields=['company_id']),
            models.Index(fields=['invoice_id']),
        ]