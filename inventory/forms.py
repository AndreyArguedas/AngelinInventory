
from django import forms
from django.forms import inlineformset_factory
from .models import Product, Event, EventProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity', 'price']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'cost']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

EventProductFormSet = inlineformset_factory(
    Event,
    EventProduct,
    fields=('product', 'quantity'),
    extra=1,  # allow at least 3 product rows by default
    can_delete=True,
    widgets={
        'quantity': forms.NumberInput(attrs={'min': 1}),
    }
)

class EventDateFilterForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

