from django import forms
from django.core.exceptions import ValidationError
from Labtechnician.models import Add_test
class AddtestForm(forms.ModelForm):
    test_type = forms.CharField(label="Test Name",widget=forms.TextInput(attrs={'class':'form-control'}

    ) ,max_length=30,required=True)
    fees = forms.CharField(label="Test Fees",widget=forms.TextInput(attrs={'class':'form-control'}

    ) ,max_length=30,required=True)

    class Meta:
        model = Add_test
        fields = ("test_type","fees")
    def clean_test_type(self,*args, **kwargs):
        test_type = self.cleaned_data.get('test_type')
        if Add_test.objects.filter(test_type=test_type).exists():
            raise forms.ValidationError("This test aleardy exist in database")
        return test_type
