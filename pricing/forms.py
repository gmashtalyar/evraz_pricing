from django import forms
from .models import MarketingData, MarketingData2, MarketingData3


class MarketingInputsForm(forms.ModelForm):
    class Meta:
        model = MarketingData
        fields = ['A', 'B', 'C']


class MarketingInputsForm2(forms.ModelForm):
    class Meta:
        model = MarketingData2
        fields = ['width', 'length', 'height']


class MarketingInputsForm3(forms.ModelForm):
    class Meta:
        model = MarketingData3
        fields = "__all__"

