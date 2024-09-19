from django.db import models

class Factura(models.Model):
    id                    = models.AutoField(primary_key=True)
    company_id            = models.BigIntegerField(null=True)
    
    tipo_factura          = models.CharField(max_length=3, null=True)
    name_factura          = models.CharField(max_length=40, null=True)
    apunta_factura        = models.CharField(max_length=40, null=True)
    
    ejercicio             = models.CharField(max_length=7, null=True)
    serie_fact            = models.CharField(max_length=22, null=True)
    numero                = models.BigIntegerField(null=True)                           
    serie_fact_unique     = models.CharField(max_length=22, null=True, unique=True)

    customer_id           = models.BigIntegerField(null=True)
    customer_num          = models.BigIntegerField(null=True)
    receptor_company_name = models.CharField(max_length=222, null=True)
                                                                                        # 1.Número de factura y, en su caso, serie.
    
    fecha_expedicion      = models.CharField(max_length=33, null=True)                  # 2.Fecha de expedición.
    vencimiento           = models.CharField(max_length=33, null=True)
            
                                                                                        # 3.Nombre y apellidos, razón o denominación social tanto del emisor como del receptor de la factura.
                                                                                        # 4. Número de identificación fiscal (NIF) de ambas partes.
                                                                                        # 5. Domicilio del emisor y del receptor.
                                                                                        # 6. Descripción de las operaciones para determinar la base imponible del impuesto.
                                                                                        # 7. Precio unitario de las operaciones. Es decir, sin incluir impuestos.
    
                                                                                        # 8. El tipo impositivo que se aplica, así como la cuota tributaria.
                                                                                        # 9. La fecha en la que se hayan efectuado las operaciones siempre que se trate de una fecha distinta a la de expedición de la factura.

    
    ivas_desglose   = models.CharField(max_length=1000, null=True) 
   
    importe_ivas     = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    subtotal         = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    total            = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    total2           = models.DecimalField(max_digits=11, decimal_places=2, default=0)
  
    observacion      = models.CharField(max_length=254, null=True)



    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['company_id']),
        ]