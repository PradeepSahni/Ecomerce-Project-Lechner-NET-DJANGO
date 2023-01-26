from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def moldingtools(request):
    print("Hello pradeep")
    context = {"name":"pradeep"}
    return render(request, 'moldingtool/moldingtools.html', context=context)

@login_required 
def add_moldingtool(request):
    error_message = {}
    input_data = {}
    return render(request,'moldingtool/add_moldingtool.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_moldingtool(request,product_id):
    messages.success(request, 'Customer deleted SuccessFully.')
    return redirect('/moldingtools')
@login_required
def edit_moldingtool(request,product_id):
    error_message = {}
    data = {}
    return render(request,"moldingtool/edit_moldingtool.html",{"error":error_message,'data':data})
