from invoice.models.company import Company
from ..utils.util_suzdal import json_suzdal
from ..utils.time_suzdal import time_suzdal
from ..utils.time_suzdal import second_suzdal

def try_register(request):
    try:

        cif      = request.POST.get('cif').strip()
        email    = request.POST.get('email').strip()
        tlf      = request.POST.get('tlf').strip()
        password = request.POST.get('password').strip()

        company, createdTrue = Company.objects.get_or_create(cif=cif, email=email, password=password)
        company.tlf = tlf
        company.numvisit += 1

        if createdTrue:
            company.state   = 'activo'
            company.regtime = time_suzdal()
            company.uid     = second_suzdal()
        
        company.lastvisit   = time_suzdal()
        company.save()

        rdata = {
            'cif': company.cif,
            'email': company.email,
            'password': company.password,
            'status': 'ok',
        }

        res = json_suzdal(rdata)
        return res
    
    except Exception as e:
            return json_suzdal({'message': str(e),'status': 'error'})


