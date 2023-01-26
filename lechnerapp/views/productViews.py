from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from barcode import EAN13 
from barcode.writer import ImageWriter



@login_required
def products(request):
    print("Hello pradeep")
    context = {"name":"pradeep"}
    return render(request, 'product/products.html', context=context)

@login_required 
def add_product(request):
    error_message = {}
    input_data = {}
    return render(request,'product/add_product.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_product(request,product_id):
    messages.success(request, 'Customer deleted SuccessFully.')
    return redirect('/products')
@login_required
def edit_product(request,product_id):
    error_message = {}
    data = {}
    return render(request,"product/edit_product.html",{"error":error_message,'data':data})
def getbarcode(request):
    number = '5901234123457'
    my_code = EAN13(number, writer=ImageWriter())
    my_code.save("new_code1")
    return my_code
