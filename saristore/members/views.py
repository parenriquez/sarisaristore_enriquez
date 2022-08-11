from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from members.models import Product, Sale
from members.forms import UpdateStockForm, SaleForm,  AddNewItemForm
# Create your views here.

#returns all the Product table details
def home(request):
    products = Product.objects.all().order_by('-id')

    return render(request,
                  'products/index.html',
                  {'products': products})

#returns a template to show the details of the product clicked
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 
                 'products/product_detail.html',
                 {'product': product})

#returns the change in item quantity once an order is made
def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)  

    if request.method == 'POST':     
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price   
            new_sale.save()
            #Keeps track of the stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            if issued_quantity < issued_item.total_quantity:
                issued_item.total_quantity -= issued_quantity
                issued_item.save()

                print(issued_item.item_name)
                print(request.POST['quantity'])
                print(issued_item.total_quantity)

                return redirect('receipt') 

    return render (request, 'products/issue_item.html',
                     {
                        'sales_form': sales_form,
                    })
       
#Modifies an item in the product table by allowing the user to define a new name, price, and additional
#quantity to be added to the current quantity of that item
def update_stock(request, pk):
    issued_item = Product.objects.get(id = pk)
    form = UpdateStockForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            updated_name = request.POST['item_name']
            updated_price = request.POST['unit_price']
            added_quantity = request.POST['received_quantity']
            if updated_name is not "":
                issued_item.item_name = updated_name
            else:
                issued_item.item_name = issued_item.item_name
            issued_item.unit_price = float(updated_price)
            issued_item.total_quantity += int(added_quantity)
            issued_item.clean()
            issued_item.save()

            #To add to the remaining stock quantity is reducing
            print(added_quantity)
            print(issued_item.item_name)
            print(issued_item.unit_price)
            print (issued_item.total_quantity)
            return redirect('home')

    return render (request, 'products/update_stock.html', {'form': form})

#deletes an item in the Product table
def delete_stock(request,pk):
    issued_item = Product.objects.get(id = pk)
    issued_item.delete()
    return HttpResponseRedirect(reverse('home'))

#updates the Product table by adding a new item - name, quantity, and price
def add_new_stock(request):
    newform = AddNewItemForm(request.POST)

    if request.method == 'POST':
        if newform.is_valid():
            item_name = request.POST['item_name']
            total_quantity= int(request.POST['total_quantity'])
            unit_price= float(request.POST['unit_price'])
            product=Product(item_name=item_name, total_quantity=total_quantity, unit_price=unit_price)
            product.save()
            print(product)
            return redirect('home')

    return render (request, 'products/add_new_stock.html', {'newform': newform})

#returns the immediate receipt of the current sale, together with other receipts from previous sales
def receipt(request): 
    sales = Sale.objects.all().order_by('-id')
    return render(request, 
    'products/receipt.html', 
    {'sales': sales,
    })

#returns the order summary of the particular sale transaction
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'products/receipt_detail.html', {'receipt': receipt})

#returns a sales summary of the sari-sari store using the Sales table
def all_sales(request):
    sales = Sale.objects.all()
    total  = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'products/all_sales.html',
     {
     'sales': sales, 
     'total': total,
     'change': change, 
     'net': net,
      })