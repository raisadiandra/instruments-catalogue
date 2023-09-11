from django.shortcuts import render
from .models import Product

def show_main(request):
    product = Product(
        name='Piano',
        amount=10,
        description='The piano is a keyboard instrument that produces sound when pressed on the keys.',
        price=10000000)
    
    product.save()

    context = {
        'name': 'Raisa Diandra Survijanto',
        'class': 'PBP E',
        'product': product,
    }

    return render(request, "main.html", context)