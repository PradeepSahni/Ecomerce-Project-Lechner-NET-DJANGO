from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def externalparts(request):
    print("Hello pradeep")
    context = {"name":"pradeep"}
    return render(request, 'externalpart/externalparts.html', context=context)

@login_required 
def add_externalpart(request):
    error_message = {}
    input_data = {}
    return render(request,'externalpart/add_externalpart.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_externalpart(request,product_id):
    messages.success(request, 'Customer deleted SuccessFully.')
    return redirect('/externalparts')
@login_required
def edit_externalpart(request,product_id):
    error_message = {}
    data = {}
    return render(request,"externalpart/edit_externalpart.html",{"error":error_message,'data':data})

