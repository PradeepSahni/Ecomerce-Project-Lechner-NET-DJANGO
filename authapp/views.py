from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import first
from .forms import UserRegistration, UserEditForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from authapp.models import Supplier
from authapp.models import UserDetails


@login_required
def dashboard(request):
    context = {"welcome": "Welcome to your dashboard"}
    return render(request, 'index.html', context=context)
@login_required
def users(request):
    # User = get_user_model()
    user_list = User.objects.filter(is_superuser='0')
    return render(request, 'users.html',{"users":user_list})

@login_required
def delete_user(request,user_id):
    getUserdetails = UserDetails.objects.filter(user_id=user_id)
    if getUserdetails:
        UserDetails.objects.filter(user_id=user_id).delete()
    getUser = User.objects.filter(id=user_id)
    if getUser:
        User.objects.filter(id=user_id).delete()
    messages.success(request, 'User deleted SuccessFully.')
    return redirect('/users')
@login_required
def edit_user(request,user_id):
    error_message = {}
    getUser = {}
    if user_id:
        getUser = User.objects.get(id=user_id)
    if request.method == "POST" and user_id:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        if not first_name:
            error_message['first_name'] = "first name is required"
        if not last_name:
            error_message['last_name'] = "last name is required"
        if not email:
            error_message['email'] = "email is required"
        if not username:
            error_message['username'] = "username is required"
        if not phone:
            error_message['phone'] = "phone is required"
        if not dob:
            error_message['dob'] = "birthday is required"
        if not address:
            error_message['address'] = "address is required"
        if len(error_message)==0:
            getUser = User.objects.filter(id=user_id)
            getUser.update(first_name=first_name,last_name=last_name,email=email,username=username)
            detail = UserDetails.objects.filter(user_id=user_id)
            detail.update(dob=dob,address=address,phone=phone)
            messages.success(request, 'User updated SuccessFully.')
            return redirect('/users')
    return render(request,"edit_user.html",{"error":error_message,'getUser':getUser})
@login_required
def register(request):
    error_message = {}
    input_data = {}
    if request.method == 'POST':
        # first_name = request.POST.get('first_name')
        # first_name = request.POST.get('last_name')
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            messages.success(request, 'User Created Successfully')
            return redirect('/users')
        
    else:
        form = UserRegistration()

    context = {"form": form}
    # return render(request, 'add_user.html', {'context':context,"error":error_message,'input_data':input_data})
    return render(request, 'add_user.html', context=context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/edit.html', context=context)

@login_required
def suppliers(request):
    supplier_list = Supplier.objects.filter(type='supplier')
    # get(type="supplier").all()
    return render(request,'supplier/suppliers.html',{"supplier_list":supplier_list})

def add_supplier(request):
    error_message = {}
    input_data = {}
    if request.method == "POST":
        name = request.POST.get('name')
        legal_form = request.POST.get('legal_form')
        categories = request.POST.get('categories')
        website = request.POST.get('website')
        internal_number = request.POST.get('internal_number')
        phone = request.POST.get('phone')
        if not name:
            error_message['name'] = "name is required"
        if not legal_form:
            error_message['legal_form'] = "legal form is required"
        if not categories:
            error_message['categories'] = "categories is required"
        if not website:
            error_message['website'] = "website is required"
        if not internal_number:
            error_message['internal_number'] = "internal number is required"
        if not phone:
            error_message['phone'] = "phone is required"
        input_data = request.POST
        if len(error_message) == 0:
            data = Supplier(name=name,legal_form=legal_form,website=website,internal_number=internal_number,phone=phone,categories=categories,type="supplier")
            data.save()
            messages.success(request, 'Supplier Created SuccessFully.')
            return redirect('/suppliers')
    return render(request,'supplier/add_supplier.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_supplier(request,supplier_id):
    getUserdetails = Supplier.objects.filter(id=supplier_id)
    if getUserdetails:
        Supplier.objects.filter(id=supplier_id).delete()
    messages.success(request, 'Supplier deleted SuccessFully.')
    return redirect('/suppliers')
@login_required
def edit_supplier(request,supplier_id):
    error_message = {}
    data = {}
    if supplier_id:
        data = Supplier.objects.get(id=supplier_id)
    if request.method=="POST":
        name = request.POST.get('name')
        legal_form = request.POST.get('legal_form')
        categories = request.POST.get('categories')
        website = request.POST.get('website')
        internal_number = request.POST.get('internal_number')
        phone = request.POST.get('phone')
        if not name:
            error_message['name'] = "name is required"
        if not legal_form:
            error_message['legal_form'] = "legal form is required"
        if not categories:
            error_message['categories'] = "categories is required"
        if not website:
            error_message['website'] = "website is required"
        if not internal_number:
            error_message['internal_number'] = "internal number is required"
        if not phone:
            error_message['phone'] = "phone is required"
        if len(error_message) == 0:
            data = Supplier.objects.filter(id=supplier_id)
            data.update(name=name,legal_form=legal_form,website=website,internal_number=internal_number,phone=phone,categories=categories,type="supplier")
            messages.success(request, 'Supplier Updated SuccessFully.')
            return redirect('/suppliers')
    return render(request,"supplier/edit_supplier.html",{"error":error_message,'data':data})
    
@login_required
def customers(request): 
    customers_list = {}
    # customers_list = Supplier.objects.get(type="customer")
    customers_list = Supplier.objects.filter(type='customer')
    return render(request,'customer/customers.html',{"customer_list":customers_list})
@login_required
def add_customer(request):
    error_message = {}
    input_data = {}
    if request.method == "POST":
        name = request.POST.get('name')
        legal_form = request.POST.get('legal_form')
        uid = request.POST.get('uid')
        website = request.POST.get('website')
        internal_number = request.POST.get('internal_number')
        phone = request.POST.get('phone')
        if not name:
            error_message['name'] = "name is required"
        if not legal_form:
            error_message['legal_form'] = "legal form is required"
        if not uid:
            error_message['uid'] = "UID is required"
        if not website:
            error_message['website'] = "website is required"
        if not internal_number:
            error_message['internal_number'] = "internal number is required"
        if not phone:
            error_message['phone'] = "phone is required"
        input_data = request.POST
        if len(error_message) == 0:
            data = Supplier(name=name,legal_form=legal_form,website=website,internal_number=internal_number,phone=phone,uid=uid,type="customer")
            data.save()
            messages.success(request, 'Customer Created SuccessFully.')
            return redirect('/customers')
    return render(request,'customer/add_customer.html',{"error":error_message,'input_data':input_data})
@login_required
def delete_customer(request,customer_id):
    getdetails = Supplier.objects.filter(id=customer_id)
    if getdetails:
        Supplier.objects.filter(id=customer_id).delete()
    messages.success(request, 'Customer deleted SuccessFully.')
    return redirect('/customers')
@login_required
def edit_customer(request,customer_id):
    error_message = {}
    data = {}
    if customer_id:
        data = Supplier.objects.get(id=customer_id)
    if request.method=="POST":
        name = request.POST.get('name')
        legal_form = request.POST.get('legal_form')
        uid = request.POST.get('uid')
        website = request.POST.get('website')
        internal_number = request.POST.get('internal_number')
        phone = request.POST.get('phone')
        if not name:
            error_message['name'] = "name is required"
        if not legal_form:
            error_message['legal_form'] = "legal form is required"
        if not uid:
            error_message['uid'] = "UID is required"
        if not website:
            error_message['website'] = "website is required"
        if not internal_number:
            error_message['internal_number'] = "internal number is required"
        if not phone:
            error_message['phone'] = "phone is required"
        if len(error_message) == 0:
            data = Supplier.objects.filter(id=customer_id)
            data.update(name=name,legal_form=legal_form,website=website,internal_number=internal_number,phone=phone,uid=uid,type="customer")
            messages.success(request, 'Customer Updated SuccessFully.')
            return redirect('/customers')
    return render(request,"customer/edit_customers.html",{"error":error_message,'data':data})