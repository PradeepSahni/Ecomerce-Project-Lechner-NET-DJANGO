from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def materials(request):
    print("Hello pradeep")
    context = {"name":"pradeep"}
    return render(request, 'material/materials.html', context=context)

@login_required 
def add_material(request):
    error_message = {}
    input_data = {}
    return render(request,'material/add_material.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_material(request,product_id):
    messages.success(request, 'Customer deleted SuccessFully.')
    return redirect('/materials')
@login_required
def edit_material(request,product_id):
    error_message = {}
    data = {}
    return render(request,"material/edit_material.html",{"error":error_message,'data':data})
