from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lechnerapp.models import Product
from django.core.exceptions import ValidationError
from barcode import EAN13 
from barcode.writer import ImageWriter
import uuid
from django.conf import settings
from common import helper

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'product/products.html', {"products":products})
def createBarCode():
    # number = '5901234123457'
    number = str(uuid.uuid1().int)[0:13]
    my_code = EAN13(number,writer=ImageWriter())
    bar_code = "barcode_"+uuid.uuid1().hex[0:5]
    barcode_dir = 'media/barcode/'
    my_code.save(barcode_dir+bar_code)
    product_bar_code = barcode_dir+bar_code+'.png'
    return product_bar_code

def productValidation(request):
    error_message = {}
    product_name = request.POST.get('product_name')
    product_number = request.POST.get('product_number')
    product_step = request.POST.get('product_step')
    product_quantity = request.POST.get('product_quantity')
    date = request.POST.get('date')
    ware_house = request.POST.get('ware_house')
    row_number = request.POST.get('row_number')
    product_location = request.POST.get('product_location')
    quantity_date = request.POST.get('quantity_date')
    if not product_name:
        error_message['product_name'] = "product name is required"
    if not product_number:
        error_message['product_number'] = "product number is required"
    if not product_step:
        error_message['product_step'] = "product step is required"
    if not product_quantity:
        error_message['product_quantity'] = "product quantity is required"
    if(product_quantity and not helper.isNum(product_quantity)):
        error_message['product_quantity'] = "product quantity must be numeric"
    if not date:
        error_message['date'] = "date is required"
    if not ware_house:
        error_message['ware_house'] = "ware house is required"
    if not row_number:
        error_message['row_number'] = "row number is required"
    if(row_number and not helper.isNum(row_number)):
        error_message['row_number'] = "row number must be numeric"
    if not product_location:
        error_message['product_location'] = "product location is required"
    if not quantity_date:
        error_message['quantity_date'] = "quantity date is required"
    return error_message
@login_required 
def add_product(request):
    error_message = {}
    input_data = {}
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_number = request.POST.get('product_number')
        product_step = request.POST.get('product_step')
        product_quantity = request.POST.get('product_quantity')
        date = request.POST.get('date')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        product_location = request.POST.get('product_location')
        quantity_date = request.POST.get('quantity_date')
        error_message = productValidation(request)
        input_data = request.POST
        if len(error_message) == 0:
            product_bar_code = createBarCode()
            data = Product(product_name=product_name,product_number=product_number,product_step=product_step,product_quantity=product_quantity,
            date=date,ware_house=ware_house,row_number=row_number,product_location=product_location,quantity_date=quantity_date,product_bar_code=product_bar_code)
            data.save()
            messages.success(request, 'Product Created SuccessFully.')
            return redirect('/products')
    return render(request,'product/add_product.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_product(request,product_id):
    getdetails = Product.objects.filter(id=product_id)
    if getdetails:
        Product.objects.filter(id=product_id).delete()
    messages.success(request, 'Product deleted SuccessFully.')
    return redirect('/products')
@login_required
def edit_product(request,product_id):
    error_message = {}
    data = {}
    if product_id:
        data = Product.objects.get(id=product_id)
    if request.method=="POST":
        product_name = request.POST.get('product_name')
        product_number = request.POST.get('product_number')
        product_step = request.POST.get('product_step')
        product_quantity = request.POST.get('product_quantity')
        date = request.POST.get('date')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        product_location = request.POST.get('product_location')
        quantity_date = request.POST.get('quantity_date')
        error_message = productValidation(request)
        if len(error_message) == 0:
            if data.product_bar_code:
                file_name = str(settings.BASE_DIR)+'\media\\barcode\\'+str(data.product_bar_code)
                helper.delete_file(file_name)
            product_bar_code = createBarCode()
            data = Product.objects.filter(id=product_id)
            data.update(product_name=product_name,product_number=product_number,product_step=product_step,product_quantity=product_quantity,
            date=date,ware_house=ware_house,row_number=row_number,product_location=product_location,quantity_date=quantity_date,product_bar_code=product_bar_code)
            messages.success(request, 'Product Updated SuccessFully.')
            return redirect('/products')
    return render(request,"product/edit_product.html",{"error":error_message,'data':data})
