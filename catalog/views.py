from django.shortcuts import render

from catalog.models import Product


def home(request):
    home = Product.objects.all()
    context = {"home": home}
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'contacts.html')



