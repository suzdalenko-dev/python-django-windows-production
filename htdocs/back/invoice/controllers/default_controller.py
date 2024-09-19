from invoice.models.company import Company
from invoice.models.factura import Factura
from invoice.models.customer import Customer
from invoice.models.article import Article
from ..utils.util_suzdal import create_new_article, create_new_customer, json_suzdal, update_company_data, update_old_article, upgrade_existing_customer, user_auth


def default_actions(request, action, entity, id):
    auth_status, company = user_auth(request, None)
    if auth_status is None or company is None:
        return json_suzdal({'login': False, 'status':'error', 'message':'Usuario no esta logeado'})
    
    try:
        response = []

        if action == 'get' and entity == 'factura':
            facturas = Factura.objects.filter(company_id=company['id']).order_by('-id').values('id', 'fecha_expedicion', 'serie_fact', 'receptor_company_name', 'subtotal', 'importe_ivas', 'total')
            response = list(facturas)
    
        elif action == 'get' and entity == 'cliente':
            if id == 0:
                clientes = Customer.objects.filter(company_id=company['id']).order_by('-clientcode').values('id', 'clientcode', 'razon', 'cif_nif', 'person_name', 'city', 'phone')
            else:
                clientes = Customer.objects.filter(id=id, company_id=company['id']).order_by('-id').values('id', 'clientcode', 'razon', 'cif_nif', 'person_name', 'emailcustomer', 'phone', 'country', 'province', 'zipcode', 'city', 'address')
            response = list(clientes)

        elif action == 'get' and entity == 'articulo':
            if id == 0:
                articulos = Article.objects.filter(company_id=company['id']).order_by('-artcode').values('id', 'description', 'price', 'artcode', 'iva', 'ivatype',)
            else:
                articulos = Article.objects.filter(id=id, company_id=company['id']).order_by('-id').values('id', 'description', 'price', 'artcode', 'iva', 'ivatype')
            response = list(articulos)

        elif action == 'get' and entity == 'empresa':
                response += [company]

        elif action == 'put' and entity == 'empresa':
            updated_status, company = update_company_data(request)
            response += [company]
            if updated_status is None:
                return json_suzdal({'message': 'Error en la actualizacion de la empresa', 'status': 'error', 'company':company})

        elif action == 'put' and entity == 'articulo':
            if id == 0:
                created_status = create_new_article(request)
            else:
                created_status = update_old_article(request, id)
            if created_status is None:
                return json_suzdal({'message': 'Error en la creacíon de artículo', 'status': 'error', 'company':company})
        
        elif action == 'put' and entity == 'cliente':
            if id == 0:
                customer_status = create_new_customer(request)
            else:
                customer_status = upgrade_existing_customer(request, id)
            if customer_status is None:
                return json_suzdal({'message': 'Error en la creacíon o actualizacíon del cliente ', 'status': 'error', 'company':company})

        else:
            return json_suzdal({'message': 'No existe accion o identidad', 'status': 'error', 'company':company})

        return json_suzdal({'res':response, 'status':'ok', 'company':company})
    
    except Exception as e:
        print(str(e))
        return json_suzdal({'message': str(e),'status': 'error'})
  