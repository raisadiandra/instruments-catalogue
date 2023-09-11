from django.shortcuts import render
from .models import Item

def show_main(request):
    item = Item(
        name='Piano',
        amount=10,
        description='The piano is a keyboard instrument that produces sound when pressed on the keys.',
        price=10000000)
    
    item.save()

    context = {
        'name': 'Raisa Diandra Survijanto',
        'class': 'PBP E',
        'item': item,
    }

    return render(request, "main.html", context)