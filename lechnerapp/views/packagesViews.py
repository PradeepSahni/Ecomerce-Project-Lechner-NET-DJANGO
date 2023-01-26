from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def packages(request):
    print("Hello pradeep")
    context = {"name":"pradeep"}
    return render(request, 'package/packages.html', context=context)

@login_required 
def add_package(request):
    error_message = {}
    input_data = {}
    return render(request,'package/add_package.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_package(request,product_id):
    messages.success(request, 'Customer deleted SuccessFully.')
    return redirect('/packages')
@login_required
def edit_package(request,product_id):
    error_message = {}
    data = {}
    return render(request,"package/edit_package.html",{"error":error_message,'data':data})
