from django.shortcuts import render
from .models import Product
from .forms import RawProductForm

# Create your views here.
def product_detailed_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

def product_create_view(request, *args, **kwargs):
    my_form = RawProductForm()
    context = {
        'form': my_form
    }
    return render(request, 'products/product_create.html', context)
