from django.shortcuts import render
from .csv_handler import CSV_Interface
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# have to mention the app address to get to data folder
products_interface = CSV_Interface('./pet_shop_app/data/products.csv')
# print(products_interface.all_data)
shopping_cart_interface = CSV_Interface('./pet_shop_app/data/shopping_cart.csv')


def index(request):
    
    # make sure to put the variables here 
    data = products_interface.get_data()
    return render(request, 'index.html', {'products': data})

@csrf_exempt
def add_product(request, id):
    
    if request.method == 'POST':
        print(id)
    
    return HttpResponseRedirect('/shopping-cart/')

def shopping_cart(request):
    existing_cart = shopping_cart_interface.all_data
    all_products = products_interface.all_data
    
    existing_cart_with_product_data = []
    for item in existing_cart:
        
        for product in all_products:
            if product['id'] == item['id']:
                data = {'product':product, 'quantity':item['quantity']}
                existing_cart_with_product_data.append(data)
    
    return render(request, 'shopping_cart.html',{'cart': existing_cart_with_product_data})
