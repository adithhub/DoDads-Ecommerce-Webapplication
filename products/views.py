from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.http import HttpResponseNotFound


def get_product(request, slug):
    print('******')
    print(request.user)
    print('******')
    print(request.user.profile.get_cart_count)
    try:
        product = get_object_or_404(Product, slug=slug)
        context = {'product': product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_by_price(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(price)
        return render(request, 'product/product.html', context=context)
    except Exception as e:
        print(e)
        return HttpResponseNotFound('Product not found')
