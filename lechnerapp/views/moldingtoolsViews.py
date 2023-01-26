from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lechnerapp.models import MoldingTool
from authapp.models import Supplier
from common import helper

@login_required
def moldingtools(request):
    moldingTools = MoldingTool.objects.all()
    return render(request, 'moldingtool/moldingtools.html',{'moldingTools':moldingTools})
def moldingtoolsValidation(request):
    error_message = {}
    molding_name = request.POST.get('molding_name')
    molding_number = request.POST.get('molding_number')
    supplier_id = request.POST.get('supplier_id')
    date = request.POST.get('date')
    ware_house = request.POST.get('ware_house')
    row_number = request.POST.get('row_number')
    molding_location = request.POST.get('molding_location')
    if not molding_name:
        error_message['molding_name'] = "molding name is required"
    
    if not molding_number:
        error_message['molding_number'] = "molding number is required"
    if(molding_number and not helper.isNum(molding_number)):
        error_message['molding_number'] = "molding number must be numeric"
    if not supplier_id:
        error_message['supplier_id'] = "owner/supplier is required"
    if(supplier_id and not helper.isNum(supplier_id)):
        error_message['supplier_id'] = "owner/supplier must be numeric"
    if not date:
        error_message['date'] = "date is required"
    if not ware_house:
        error_message['ware_house'] = "ware house is required"
    if not row_number:
        error_message['row_number'] = "row number is required"
    if(row_number and not helper.isNum(row_number)):
        error_message['row_number'] = "row number must be numeric"
    if not molding_location:
        error_message['molding_location'] = "material location is required"
    return error_message

@login_required 
def add_moldingtool(request):
    error_message = {}
    input_data = {}
    suppliers = Supplier.objects.all()
    if request.method == "POST":
        molding_name = request.POST.get('molding_name')
        molding_number = request.POST.get('molding_number')
        supplier_id = request.POST.get('supplier_id')
        date = request.POST.get('date')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        molding_location = request.POST.get('molding_location')
        error_message = moldingtoolsValidation(request)
        input_data = request.POST
        if len(error_message) == 0:
            data = MoldingTool(molding_name=molding_name,molding_number=molding_number,supplier_id=supplier_id,
            date=date,ware_house=ware_house,row_number=row_number,molding_location=molding_location)
            data.save()
            messages.success(request, 'Molding Tool Created SuccessFully.')
            return redirect('/moldingtools')
    return render(request,'moldingtool/add_moldingtool.html',{"error":error_message,'input_data':input_data,'suppliers':suppliers})
@login_required
def delete_moldingtool(request,moldingtool_id):
    getdetails = MoldingTool.objects.filter(id=moldingtool_id)
    if getdetails:
        MoldingTool.objects.filter(id=moldingtool_id).delete()
    messages.success(request, 'Molding Tool deleted SuccessFully.')
    return redirect('/moldingtools')
@login_required
def edit_moldingtool(request,moldingtool_id):
    error_message = {}
    data = {}
    suppliers = Supplier.objects.all()
    if moldingtool_id:
        data = MoldingTool.objects.get(id=moldingtool_id)
    if request.method=="POST":
        molding_name = request.POST.get('molding_name')
        molding_number = request.POST.get('molding_number')
        supplier_id = request.POST.get('supplier_id')
        date = request.POST.get('date')
        ware_house = request.POST.get('ware_house')
        row_number = request.POST.get('row_number')
        molding_location = request.POST.get('molding_location')
        error_message = moldingtoolsValidation(request)
        if len(error_message) == 0:
            update_data = MoldingTool.objects.filter(id=moldingtool_id)
            update_data.update(molding_name=molding_name,molding_number=molding_number,supplier_id=supplier_id,
            date=date,ware_house=ware_house,row_number=row_number,molding_location=molding_location)
            messages.success(request, 'molding tools updated SuccessFully.')
            return redirect('/moldingtools')
    return render(request,"moldingtool/edit_moldingtool.html",{"error":error_message,'data':data,'suppliers':suppliers})
