from django.shortcuts import render
from item.models import Category,Item

# Create your views here.
def index(request):
    items=Item.objects.all()[0:6]
    Categories=Category.objects.all()
    return render(request,'core/index.html', {
        'categories':Categories,
        'items':items,
    })


def contact(request):
    return render(request, 'core/contact.html')