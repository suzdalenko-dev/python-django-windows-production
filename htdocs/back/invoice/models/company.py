from django.db import models

class Company(models.Model):
    id           = models.AutoField(primary_key=True)
    razon        = models.CharField(max_length=111, null=True)
    person_name  = models.CharField(max_length=111, null=True)
    cif          = models.CharField(max_length=33, null=True, unique=True)
    email        = models.CharField(max_length=111, null=True, unique=True) 
    emailcompany = models.CharField(max_length=111, null=True) 
    password     = models.CharField(max_length=111, null=True)
    tlf          = models.CharField(max_length=33, null=True)
    tlf2         = models.CharField(max_length=33, null=True)

    numvisit     = models.BigIntegerField(default=0)
    regtime      = models.CharField(max_length=33, null=True)
    lastvisit    = models.CharField(max_length=33, null=True)
    uid          = models.CharField(max_length=111, null=True)

    country      = models.CharField(max_length=33, null=True)
    province     = models.CharField(max_length=33, null=True)
    zipcode      = models.CharField(max_length=22, null=True)
    city         = models.CharField(max_length=33, null=True)
    address      = models.CharField(max_length=111, null=True)
    price        = models.DecimalField(max_digits=11, decimal_places=2, default=0)
   
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]