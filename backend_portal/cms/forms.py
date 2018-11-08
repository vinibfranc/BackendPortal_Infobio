from django import forms

from .models import Opportunity

class OpportunityForm(forms.ModelForm):

    class Meta:
        model = Opportunity
        fields = ('title', 'description', 'institution', 'city', 'area')