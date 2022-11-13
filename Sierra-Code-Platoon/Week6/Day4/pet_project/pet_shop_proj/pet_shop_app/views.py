from django.shortcuts import render
from .csv_handler import CSV_Interface
# Create your views here.
# have to mention the app address to get to data folder
products_interface = CSV_Interface('./data/products.csv')
# print(products_interface.all_data)

data = products_interface.all_data()
print(data)
def index(request):
    # make sure to put the variables here 

    
    return render(request, 'index.html')
