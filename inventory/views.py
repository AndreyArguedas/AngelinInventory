
from datetime import date, timedelta
from calendar import monthrange
from django.utils.timezone import now
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from .models import Event
from .forms import EventForm, EventProductFormSet, EventDateFilterForm

def intro_page(request):
    return render(request, "inventory/intro.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

def event_list(request):
    today = date.today()
    range_type = request.GET.get("range", "week")

    # Default ranges
    if range_type == "year":
        start = date(today.year, 1, 1)
        end = date(today.year, 12, 31)
    elif range_type == "month":
        start = date(today.year, today.month, 1)
        end = date(today.year, today.month, monthrange(today.year, today.month)[1])
    else:  # default to "week"
        start = today - timedelta(days=today.weekday())  # Monday
        end = start + timedelta(days=6)  # Sunday

    # Use form dates if they are manually set
    form = EventDateFilterForm(request.GET or None)
    if form.is_valid() and (form.cleaned_data.get('start_date') or form.cleaned_data.get('end_date')):
        if form.cleaned_data.get('start_date'):
            start = form.cleaned_data['start_date']
        if form.cleaned_data.get('end_date'):
            end = form.cleaned_data['end_date']

    events = Event.objects.filter(date__gte=start, date__lte=end)

    return render(request, 'inventory/event_list.html', {
        'events': events,
        'form': form,
        'current_range': range_type
    })


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        formset = EventProductFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            event = form.save()
            formset.instance = event
            formset.save()
            return redirect('event_list')
    else:
        form = EventForm()
        formset = EventProductFormSet()
    return render(request, 'inventory/event_form.html', {'form': form, 'formset': formset})