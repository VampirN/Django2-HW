from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    home = Product.objects.all()
    context = {"home": home}
    return render(request, 'base_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'contacts.html')


def product_card(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_card.html', context)



