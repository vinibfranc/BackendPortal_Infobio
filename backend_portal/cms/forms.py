from django import forms

from .models import Opportunity

class OpportunityForm(forms.ModelForm):

    '''title = models.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 

        }
    ))
    description = models.TextField()
    institution = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)'''

    class Meta:
        model = Opportunity
        fields = ('title', 'description', 'institution', 'city', 'area')