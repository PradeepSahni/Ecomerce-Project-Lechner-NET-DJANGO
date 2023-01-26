from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lechnerapp.models import Package
from lechnerapp.models import Material
from lechnerapp.models import Supplier
from lechnerapp.models import Product
from common import helper

@login_required
def packages(request):
    packageLists = Package.objects.all()
    return render(request, 'package/packages.html',{'packageLists':packageLists})
def packageValidation(request):
    error_message = {}
    package_name = request.POST.get('package_name')
    type_of_packaging = request.POST.get('type_of_packaging')
    package_number = request.POST.get('package_number')
    internal_number = request.POST.get('internal_number')
    supplier_id = request.POST.get('supplier_id')
    material_id = request.POST.get('material_id')
    dimension = request.POST.get('dimension')
    package_quantity = request.POST.get('package_quantity')
    price = request.POST.get('price')
    date = request.POST.get('date')
    product_id = request.POST.get('product_id')
    ware_house = request.POST.get('ware_house')
    row_number = request.POST.get('row_number')
    package_location = request.POST.get('package_location')
    if not package_name:
        error_message['package_name'] = "package name is required"
    if not type_of_packaging:
        error_message['type_of_packaging'] = "type of packaging is required"
    if not package_number:
        error_message['package_number'] = "package number is required"
    if package_number and not helper.isNum(package_number):
        error_message['package_number'] = "package number must be numeric"
    if not internal_number:
        error_message['internal_number'] = "internal number is required"
    if internal_number and not helper.isNum(internal_number):
        error_message['internal_number'] = "internal number must be numeric"
    if not supplier_id:
        error_message['supplier_id'] = "supplier is required"
    if not material_id:
        error_message['material_id'] = "material is required"
    if not dimension:
        error_message['dimension'] = "dimension is required"
    if not package_quantity:
        error_message['package_quantity'] = "package quantityr is required"
    if(package_quantity and not helper.isNum(package_quantity)):
        error_message['package_quantity'] = "package  quantity must be numeric"
    if not price:
        error_message['price'] = "price is required"
    if(price and not helper.isNum(price)):
        error_message['price'] = "price must be numeric"
    if not date:
        error_message['date'] = "date is required"
    if not product_id:
        error_message['product_id'] = "product is required"
    if not ware_house:
        error_message['ware_house'] = "ware house is required"
    if not row_number:
        error_message['row_number'] = "row number is required"
    if(row_number and not helper.isNum(row_number)):
        error_message['row_number'] = "row number must be numeric"
    if not package_location:
        error_message['package_location'] = "package location is required"
    return error_message
@login_required 
def add_package(request):
    error_message = {}
    input_data = {}
    materials = Material.objects.all()
    suppliers = Supplier.objects.all()
    products = Product.objects.all()
    if request.method == "POST":
        package_name = request.POST.get('package_name')
        type_of_packaging = request.POST.get('type_of_packaging')
        package_number = request.POST.get('package_number')
        internal_number = request.POST.get('internal_number')
        supplier_id = request.POST.get('supplier_id')
        material_id = request.POST.get('material_id')
        dimension = request.POST.get('dimension')
        package_quantity = request.POST.get('package_quantity')
        price = request.POST.get('price')
        date = request.POST.get('date')
        product_id = request.POST.get('product_id')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        package_location = request.POST.get('package_location')
        error_message = packageValidation(request)
        input_data = request.POST
        if len(error_message) == 0:
            data_insert = Package(package_name=package_name,type_of_packaging=type_of_packaging,package_number=package_number,
            internal_number=internal_number,supplier_id=supplier_id,material_id=material_id,dimension=dimension,package_quantity=package_quantity,
            price=price,date=date,product_id=product_id,ware_house=ware_house,row_number=row_number,package_location=package_location)
            data_insert.save()
            messages.success(request, 'New Package Created SuccessFully.')
            return redirect('/packages')
    return render(request,'package/add_package.html',{"error":error_message,'input_data':input_data,'materials':materials,'suppliers':suppliers,'products':products})
@login_required
def delete_package(request,package_id):
    getdetails = Package.objects.filter(id=package_id)
    if getdetails:
        Package.objects.filter(id=package_id).delete()
    messages.success(request, 'Package deleted SuccessFully.')
    return redirect('/packages')
@login_required
def edit_package(request,package_id):
    error_message = {}
    data = {}
    materials = Material.objects.all()
    suppliers = Supplier.objects.all()
    products = Product.objects.all()
    if package_id:
        data = Package.objects.get(id=package_id)
    if request.method=="POST":
        package_name = request.POST.get('package_name')
        type_of_packaging = request.POST.get('type_of_packaging')
        package_number = request.POST.get('package_number')
        internal_number = request.POST.get('internal_number')
        supplier_id = request.POST.get('supplier_id')
        material_id = request.POST.get('material_id')
        dimension = request.POST.get('dimension')
        package_quantity = request.POST.get('package_quantity')
        price = request.POST.get('price')
        date = request.POST.get('date')
        product_id = request.POST.get('product_id')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        package_location = request.POST.get('package_location')
        error_message = packageValidation(request)
        if len(error_message) == 0:
            update_data = Package.objects.filter(id=package_id)
            update_data.update(package_name=package_name,type_of_packaging=type_of_packaging,package_number=package_number,
            internal_number=internal_number,supplier_id=supplier_id,material_id=material_id,dimension=dimension,package_quantity=package_quantity,
            price=price,date=date,product_id=product_id,ware_house=ware_house,row_number=row_number,package_location=package_location)
            messages.success(request, 'Package updated SuccessFully.')
            return redirect('/packages')
    return render(request,"package/edit_package.html",{"error":error_message,'data':data,'materials':materials,'suppliers':suppliers,'products':products})
