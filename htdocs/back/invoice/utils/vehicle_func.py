from invoice.models.vehicledata import Vehicledata

def get_or_save_vehicle(invoice_id, company_id, customer_id, matricula, other_data):
    try:
        vehicle, _ = Vehicledata.objects.get_or_create(company_id=company_id, customer_id=customer_id, matricula=matricula)
        vehicle.invoice_id = invoice_id
        vehicle.other_data = other_data
        vehicle.save()
        print('vehicle.id='+str(vehicle.id))
        return vehicle.id
    except Exception as e:
        return 0