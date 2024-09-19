from invoice.models.company import Company
from ..utils.util_suzdal import json_suzdal
from ..utils.time_suzdal import time_suzdal


def try_login(request):
    try:

        cif      = request.POST.get('cif').strip()
        email    = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        company = Company.objects.get(cif=cif, email=email)
        if company.password != password:
            return json_suzdal({'message': 'Usuario no encotrado..', 'status': 'error'})
      
        company.lastvisit = time_suzdal()
        company.numvisit += 1
        company.save()

        rdata = {
            'company_id': company.id,
            'uid': company.uid,
            'status': 'ok',
        }

        res = json_suzdal(rdata)
        return res
    
    except Exception as e:
            return json_suzdal({'message': 'Usuario no encotrado...','status': 'error'})