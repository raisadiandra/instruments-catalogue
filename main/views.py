from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Raisa Diandra Survijanto',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)