from django import forms

from .models import Employees

class EmpForm(forms.ModelForm):

    class Meta:

        model = Employees
        fields = ('emp_id','password',)
