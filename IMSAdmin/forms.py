from django import forms
from . import models

class InsuranceCompanyForm(forms.ModelForm):
    class Meta:
        model = models.InsuranceCompany
        fields = ('name','logo',);