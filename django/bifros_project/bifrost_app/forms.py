from django import forms
from bifrost_app.models import Volume

class NewVolumeForm(forms.ModelForm):
    class Meta:
        model = Volume
        fields="__all__"
