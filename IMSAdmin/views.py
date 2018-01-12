from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import InsuranceCompanyForm
from . import models

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InsuranceCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/IMS/admin')
        else:
            return HttpResponse('Invalid!')
    else:
        company = models.InsuranceCompany.objects.first()
        form = InsuranceCompanyForm(instance=company)

    return render(request, 'IMSAdmin/insurance_company_form.html', {'form': form, 'company': company})
    #return render(request,'IMSAdmin/index.html')