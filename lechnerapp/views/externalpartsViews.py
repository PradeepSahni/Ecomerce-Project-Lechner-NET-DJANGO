from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lechnerapp.models import ExternalPart
from lechnerapp.models import Product
from lechnerapp.models import Supplier
from common import helper

@login_required
def externalparts(request):
    externalParts = ExternalPart.objects.all()
    return render(request, 'externalpart/externalparts.html',{"externalParts":externalParts})

def externalPartValidation(request):
    error_message = {}
    part_name = request.POST.get('part_name')
    part_number = request.POST.get('part_number')
    charge_number = request.POST.get('charge_number')
    supplier_id = request.POST.get('supplier_id')
    date = request.POST.get('date')
    product_id = request.POST.get('product_id')
    product_use_location = request.POST.get('product_use_location')
    ware_house = request.POST.get('ware_house')
    row_number = request.POST.get('row_number')
    part_location = request.POST.get('part_location')
    if not part_name:
        error_message['part_name'] = "part name is required"
    if not part_number:
        error_message['part_number'] = "part_number is required"
    if not charge_number:
        error_message['charge_number'] = "charge number is required"
    if not supplier_id:
        error_message['supplier_id'] = "supplier is required"
    if not date:
        error_message['date'] = "date is required"
    if not product_id:
        error_message['product_id'] = "product is required"
    if not product_use_location:
        error_message['product_use_location'] = "product use location is required"
    if not ware_house:
        error_message['ware_house'] = "ware house is required"
    if not row_number:
        error_message['row_number'] = "row number is required"
    if(row_number and not helper.isNum(row_number)):
        error_message['row_number'] = "row number must be numeric"
    if not part_location:
        error_message['part_location'] = "part location is required"
    return error_message

@login_required 
def add_externalpart(request):
    error_message = {}
    input_data = {}
    suppliers = Supplier.objects.all()
    products = Product.objects.all()
    if request.method == "POST":
        part_name = request.POST.get('part_name')
        part_number = request.POST.get('part_number')
        charge_number = request.POST.get('charge_number')
        supplier_id = request.POST.get('supplier_id')
        date = request.POST.get('date')
        product_id = request.POST.get('product_id')
        product_use_location = request.POST.get('product_use_location')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        part_location = request.POST.get('part_location')
        error_message = externalPartValidation(request)
        input_data = request.POST
        if len(error_message) == 0:
            data_insert = ExternalPart(part_name=part_name,part_number=part_number,charge_number=charge_number,
            product_use_location=product_use_location,supplier_id=supplier_id,date=date,product_id=product_id,
            ware_house=ware_house,row_number=row_number,part_location=part_location)
            data_insert.save()
            messages.success(request, 'New External Part Created SuccessFully.')
            return redirect('/externalparts')
    return render(request,'externalpart/add_externalpart.html',{"error":error_message,'input_data':input_data,'suppliers':suppliers,'products':products})
@login_required
def delete_externalpart(request,part_id):
    getdetails = ExternalPart.objects.filter(id=part_id)
    if getdetails:
        ExternalPart.objects.filter(id=part_id).delete()
    messages.success(request, 'External Part deleted SuccessFully.')
    return redirect('/externalparts')
@login_required
def edit_externalpart(request,part_id):
    error_message = {}
    data = {}
    suppliers = Supplier.objects.all()
    products = Product.objects.all()
    if part_id:
        data = ExternalPart.objects.get(id=part_id)
    if request.method=="POST":
        part_name = request.POST.get('part_name')
        part_number = request.POST.get('part_number')
        charge_number = request.POST.get('charge_number')
        supplier_id = request.POST.get('supplier_id')
        date = request.POST.get('date')
        product_id = request.POST.get('product_id')
        product_use_location = request.POST.get('product_use_location')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        part_location = request.POST.get('part_location')
        error_message = externalPartValidation(request)
        if len(error_message) == 0:
            update_data = ExternalPart.objects.filter(id=part_id)
            update_data.update(part_name=part_name,part_number=part_number,charge_number=charge_number,
            product_use_location=product_use_location,supplier_id=supplier_id,date=date,product_id=product_id,
            ware_house=ware_house,row_number=row_number,part_location=part_location)
            messages.success(request, 'External Part updated SuccessFully.')
            return redirect('/externalparts')
    return render(request,"externalpart/edit_externalpart.html",{"error":error_message,'data':data,'suppliers':suppliers,'products':products})

