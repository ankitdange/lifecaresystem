from django import forms
from Pharmist.models import Drugs
class DrugsForm(forms.ModelForm):
    
    class Meta:
        model = Drugs
        fields = ("__all__")
class Drugsupdate(forms.ModelForm):
    

    class Meta:
        model = Drugs
        fields = ("price",)