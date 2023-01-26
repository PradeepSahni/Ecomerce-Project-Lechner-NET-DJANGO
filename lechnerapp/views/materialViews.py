from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lechnerapp.models import Material
from lechnerapp.models import MaterialImage
from authapp.models import Supplier
from common import helper
import json
from django.conf import settings 

@login_required
def materials(request):
    materials = Material.objects.all()
    return render(request, 'material/materials.html',{'materials':materials})

def materialValidation(request):
    error_message = {}
    material_name = request.POST.get('material_name')
    material_type = request.POST.get('material_type')
    material_number = request.POST.get('material_number')
    supplier_id = request.POST.get('supplier_id')
    material_quantity = request.POST.get('material_quantity')
    price = request.POST.get('price')
    material_sample = request.POST.get('material_sample')
    ware_house = request.POST.get('ware_house')
    row_number = request.POST.get('row_number')
    material_location = request.POST.get('material_location')
    quantity_date = request.POST.get('quantity_date')
    if not material_name:
        error_message['material_name'] = "material name is required"
    if not material_type:
        error_message['material_type'] = "material type is required"
    if not material_number:
        error_message['material_number'] = "product number is required"
    if(material_number and not helper.isNum(material_number)):
        error_message['material_number'] = "material number must be numeric"
    if not supplier_id:
        error_message['supplier_id'] = "owner/supplier is required"
    if(supplier_id and not helper.isNum(supplier_id)):
        error_message['supplier_id'] = "owner/supplier must be numeric"
    if not material_quantity:
        error_message['material_quantity'] = "material quantity is required"
    if(material_quantity and not helper.isNum(material_quantity)):
        error_message['material_quantity'] = "material quantity must be numeric"
    if not price:
        error_message['price'] = "price is required"
    if(price and not helper.isNum(price)):
        error_message['price'] = "price must be numeric"
    if not material_sample:
        error_message['material_sample'] = "material sample is required"
    if not ware_house:
        error_message['ware_house'] = "ware house is required"
    if not row_number:
        error_message['row_number'] = "row number is required"
    if(row_number and not helper.isNum(row_number)):
        error_message['row_number'] = "row number must be numeric"
    if not material_location:
        error_message['material_location'] = "material location is required"
    if not quantity_date:
        error_message['quantity_date'] = "quantity date is required"
    return error_message

@login_required 
def add_material(request):
    error_message = {}
    input_data = {}
    suppliers = Supplier.objects.all()
    if request.method == "POST":
        material_name = request.POST.get('material_name')
        material_type = request.POST.get('material_type')
        material_number = request.POST.get('material_number')
        supplier_id = request.POST.get('supplier_id')
        material_quantity = request.POST.get('material_quantity')
        price = request.POST.get('price')
        material_sample = request.POST.get('material_sample')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        material_location = request.POST.get('material_location')
        quantity_date = request.POST.get('quantity_date')
        error_message = materialValidation(request)
        input_data = request.POST
        if len(error_message) == 0:
            if request.FILES['image']:
                filename = helper.handle_uploaded_file(request.FILES['image'],'materials')
            data = Material(material_name=material_name,material_type=material_type,material_number=material_number,supplier_id=supplier_id,material_quantity=material_quantity,
            price=price,material_sample=material_sample,ware_house=ware_house,row_number=row_number,material_location=material_location,quantity_date=quantity_date)
            data.save()
            if filename:
                material_image = MaterialImage(image=filename,material_id=data.id)
                material_image.save()
            messages.success(request, 'Material Created SuccessFully.')
            return redirect('/materials')
    return render(request,'material/add_material.html',{"error":error_message,'input_data':input_data,'suppliers':suppliers})
@login_required
def delete_material(request,material_id):
    getdetails = Material.objects.filter(id=material_id)
    if getdetails:
        # unlink File 
        data = Material.objects.get(id=material_id)
        file_name = str(settings.MEDIA_ROOT)+'/'+str(data.materialimage.image)
        helper.delete_file(file_name)
        Material.objects.filter(id=material_id).delete()
    messages.success(request, 'Material deleted SuccessFully.')
    return redirect('/materials')
@login_required
def edit_material(request,material_id):
    error_message = {}
    data = {}
    suppliers = Supplier.objects.all()
    if material_id:
        data = Material.objects.get(id=material_id)
    if request.method=="POST":
        material_name = request.POST.get('material_name')
        material_type = request.POST.get('material_type')
        material_number = request.POST.get('material_number')
        supplier_id = request.POST.get('supplier_id')
        material_quantity = request.POST.get('material_quantity')
        price = request.POST.get('price')
        material_sample = request.POST.get('material_sample')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        material_location = request.POST.get('material_location')
        quantity_date = request.POST.get('quantity_date')
        error_message = materialValidation(request)
        if len(error_message) == 0:
            if request.FILES['image']:
                filename = helper.handle_uploaded_file(request.FILES['image'],'materials')
            update_data = Material.objects.filter(id=material_id)
            update_data.update(material_name=material_name,material_type=material_type,material_number=material_number,supplier_id=supplier_id,material_quantity=material_quantity,
            price=price,material_sample=material_sample,ware_house=ware_house,row_number=row_number,material_location=material_location,quantity_date=quantity_date)
            if data.materialimage.image and filename:
                # unlink file 
                file_name = str(settings.MEDIA_ROOT)+'/'+str(data.materialimage.image)
                helper.delete_file(file_name)
                # update new uploaded file into database 
                update_image_data = MaterialImage.objects.filter(id=data.materialimage.id)
                update_image_data.update(image=filename)
            messages.success(request, 'Material updated SuccessFully.')
            return redirect('/materials')
    return render(request,"material/edit_material.html",{"error":error_message,'data':data,'suppliers':suppliers})
