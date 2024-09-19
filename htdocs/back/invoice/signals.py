from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article, Document, Customer, Factura

# añado 1 al crear un articulo para una empresa determinada
@receiver(post_save, sender=Article)
def actualizar_document(sender, instance, created, **kwargs):
    if created:
        document, _ = Document.objects.get_or_create(description='articulo_numero', company_id=instance.company_id) 
        document.value += 1
        document.save()



# observer a la hora de crear un CLIENTE NUEVO actulizo el numero de clientes en la base datos
@receiver(post_save, sender=Customer)
def actualizar_document(sender, instance, created, **kwargs):
    if created:
        document, _ = Document.objects.get_or_create(description='cliente_numero', company_id=instance.company_id) 
        document.value += 1
        document.save()

    
@receiver(post_save, sender=Factura)
def actualizar_document(sender, instance, created, **kwargs):
    if created:
        document, _ = Document.objects.get_or_create(description=instance.tipo_factura, company_id=instance.company_id, ejercicio=instance.ejercicio) 
        document.value += 1
        document.save()