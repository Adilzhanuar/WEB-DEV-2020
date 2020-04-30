<<<<<<< HEAD
from django.shortcuts import render
from django.http import JsonResponse

from django.http import HttpResponse

from api.models import Category, Product


def main(request):
    return HttpResponse("""<h1>Welcome to Ayana\'s jewerly website!!</h1>
    <br><h2>Here you can find any beautiful and luxury jewerly on YOUR choice!</h2>
    <h2>To see categories type in url api/categories</h2>
    <h2>To see category detail type api/categories/id(of category)</h2>
    <h2>To see products of category type api/categories/id/products</h2>
    <h2>To see all products type api/products</h2>
    <h2>To see product\'s details type api/products/id</h2>
    """)

def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())

def category_product(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    json_products = [p.short() for p in products]
    return JsonResponse(json_products, safe=False)

def product_list(request):
    # select * from products;
    products = Product.objects.all()
    products_json = [product.short() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
       product = Product.objects.get(id=product_id)
       product_full=product.full()
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.full())
=======
from django.shortcuts import render
from django.http import JsonResponse

from django.http import HttpResponse

from api.models import Category, Product


def main(request):
    return HttpResponse("""<h1>Welcome to Ayana\'s jewerly website!!</h1>
    <br><h2>Here you can find any beautiful and luxury jewerly on YOUR choice!</h2>
    <h2>To see categories type in url api/categories</h2>
    <h2>To see category detail type api/categories/id(of category)</h2>
    <h2>To see products of category type api/categories/id/products</h2>
    <h2>To see all products type api/products</h2>
    <h2>To see product\'s details type api/products/id</h2>
    """)

def category_list(request):
    categories = Category.objects.all()
    json_categories = [c.to_json() for c in categories]
    return JsonResponse(json_categories, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())

def category_product(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    json_products = [p.short() for p in products]
    return JsonResponse(json_products, safe=False)

def product_list(request):
    # select * from products;
    products = Product.objects.all()
    products_json = [product.short() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
       product = Product.objects.get(id=product_id)
       product_full=product.full()
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.full())
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
