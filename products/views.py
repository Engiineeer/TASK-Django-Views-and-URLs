from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product


def get_home(request):
    return HttpResponse("<h1>Hello, World!</h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(
        f"<h1>product name {product.name} and price{product.price}</h1>"
    )
