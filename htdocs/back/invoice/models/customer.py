from django.db import models

class Customer(models.Model):
    id           = models.AutoField(primary_key=True)
    company_id   = models.BigIntegerField(null=True)
    clientcode   = models.PositiveBigIntegerField(default=0)
        
    cif_nif       = models.CharField(max_length=33, null=True)
    razon         = models.CharField(max_length=255, null=True)
    person_name   = models.CharField(max_length=255, null=True)
    emailcustomer = models.CharField(max_length=111, null=True)
    phone         = models.CharField(max_length=33, null=True)

    country      = models.CharField(max_length=111, default='España')
    province     = models.CharField(max_length=111, null=True)
    zipcode      = models.CharField(max_length=11, null=True)
    city         = models.CharField(max_length=111, null=True)
    address      = models.CharField(max_length=255, null=True)
    
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['company_id']),
            models.Index(fields=['cif_nif']),
        ]