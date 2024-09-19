from datetime import datetime
import json
import os
from xhtml2pdf import pisa
from invoice.models.customer import Customer
from invoice.models.factura import Factura
from invoice.models.facturalineas import Facturalineas
from invoice.models.vehicledata import Vehicledata
from invoice.utils.time_suzdal import creating_invoice_time, second_suzdal
from mysite import settings
from ..utils.util_suzdal import factura_new_article, factura_new_lines, json_suzdal, user_auth

def pdf_work(request, action, id):
    try:
        auth_status, company = user_auth(request, None)
        if auth_status is None or company is None:
            return json_suzdal({'login': False, 'status':'error', 'message':'Usuario no esta logeado'})
    
        facturaObj  = Factura.objects.get(id=id, company_id=company['id'])
        customerObj = Customer.objects.get(id=facturaObj.customer_id, company_id=company['id'])
        vehicle     = Vehicledata.objects.filter(invoice_id=id, company_id=company['id']).first()
        lineasFact  = Facturalineas.objects.filter(invoice_id=id, company_id=company['id'])

        current_time = datetime.now()
        year  = str(current_time.strftime('%Y'))
        month = str(current_time.strftime('%m'))
        # dayd  = str(current_time.strftime('%m'))
        folder_path = f"mysite/media/{str(company['id'])}/{year}/{month}/"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        seconds = creating_invoice_time()
        file_name = f"f_{facturaObj.serie_fact}_{seconds}.pdf"
        file_path = folder_path+file_name

        with open('mysite/media/fac.html', 'r') as file:
            html = file.read()
    
        html = html.replace('@name_factura@', str(facturaObj.name_factura))
        html = html.replace('@numero_factura@', str(facturaObj.serie_fact))
        html = html.replace('@fecha_factura@', str(facturaObj.fecha_expedicion))
        html = html.replace('@fecha_vencimiento@', str(facturaObj.vencimiento))
        if len(str(facturaObj.apunta_factura)) > 11: html = html.replace('@apunta_a_factura@', 'APUNTA A: '+str(facturaObj.apunta_factura))
        else: html = html.replace('@apunta_a_factura@', '')
        html = html.replace('@razon@', company['razon'])
        html = html.replace('@person_name@', company['person_name'])
        html = html.replace('@province@', company['province'])
        html = html.replace('@city@', company['city'])
        html = html.replace('@zipcode@', company['zipcode'])
        html = html.replace('@address@', company['address'])
        html = html.replace('@cif@', company['cif'])
        html = html.replace('@tlf@', company['tlf'])
        
        html = html.replace('@customer_num@', str(facturaObj.customer_num))
        html = html.replace('@razon_cl@', customerObj.razon)
        html = html.replace('@person_name_cl@', customerObj.person_name)
        html = html.replace('@province_cl@', customerObj.province)
        html = html.replace('@city_cl@', customerObj.city)
        html = html.replace('@zipcode_cl@', customerObj.zipcode)
        html = html.replace('@address_cl@', customerObj.address)
        html = html.replace('@cif_nif@', customerObj.cif_nif)
        html = html.replace('@phone@', customerObj.phone)
        html = html.replace('@country@', customerObj.country)
        if vehicle:
            vehicle_data = f"""<div class="div_vehicle">
                                    <span class="datos_vehicle">DATOS DEL VEHICULO</span>
                                    <table style="border: 1px solid rgb(233, 233, 255); color: black;">
                                        <tbody><tr><td>Matricula<br>{str(vehicle.matricula)}</td><td>Marca / Modelo / Kilometros<br>{str(vehicle.other_data)}</td></tr></tbody>
                                    </table>
                                </div><br>"""
        else:
            vehicle_data = ''
        html = html.replace('@vehicle_data@', vehicle_data)

        lines_content = ''
        for linea in lineasFact:
            lines_content += """<tr><td>"""+str(linea.article_num)+"""</td><td style="width: 333px;">"""+str(linea.article_name)+"""</td><td>"""+str(linea.cantidad)+"""</td><td>"""+str(linea.precio)+"""</td><td>"""+str(linea.descuento)+"""</td><td>"""+str(linea.importe_con_descuento)+"""</td></tr>"""
        html = html.replace('@lines_content@', lines_content)

        html_ivas = ''
        json_string = json.loads(facturaObj.ivas_desglose)
        for jsonObj in json_string:
            html_ivas +=  f"""<tr><td>{jsonObj['base_imponible']:.2f}</td><td>{jsonObj['iva']}</td><td>{jsonObj['valor_iva']:.2f}</td><td>{jsonObj['recec']:.2f}</td><td>0.00</td></tr>"""
            print(jsonObj)
        
        html = html.replace('@html_ivas@', html_ivas)
        html = html.replace('@suma_importes@', f"""{facturaObj.subtotal:.2f}""")
        html = html.replace('@importe_ivas@', f"""{facturaObj.importe_ivas:.2f}""")
        html = html.replace('@factura_total@', f"""{facturaObj.total:.2f}""")
        html = html.replace('@observaciones@', str(facturaObj.observacion))

        print('-----------------'+str(file_path))

        with open(file_path, "wb") as pdf_file:
            # Convertir el HTML a PDF y guardarlo en el archivo
            pisa_status = pisa.CreatePDF(html, dest=pdf_file)

        file_path = file_path.split('media')

        rdata = {
                'status': 'ok',
                'message': 'PDF creado',
                'url':'media'+file_path[1],
                'id':id
        }
         
    
        return json_suzdal(rdata)
    
    except Exception as e:
        return json_suzdal({'message': str(e), 'status': 'error'})