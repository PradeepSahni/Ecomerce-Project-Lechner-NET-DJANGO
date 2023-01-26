from django.urls import path
# from .views import edit, dashboard, register
from . import views 
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                    PasswordResetCompleteView, PasswordResetConfirmView,
                                    PasswordChangeView, PasswordChangeDoneView,
                                    PasswordResetDoneView)


app_name = 'authapp'

urlpatterns = [
    # path('register', views.register, name='register'),
    path('edit', views.edit, name='edit'),
    path('dashboard',LoginView.as_view(template_name='index.html'), name='dashboard'),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html'), name='password_change'),
    path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
        name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='password/password_reset_form.html',
        email_template_name='password/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
        
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='password/password_reset_confirm.html',
        success_url=reverse_lazy('authapp:password_reset_complete')), name='password_reset_confirm'),
    
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    
    # User Path 
    path('users',views.users,name="users"),
    path('add_user',views.register,name="add_user"),
    path('delete_user/<int:user_id>',views.delete_user,name="delete_user"),
    path('edit_user/<int:user_id>',views.edit_user,name="edit_user"),

    #Supplier Path 
    path('suppliers',views.suppliers,name='suppliers'),
    path('add_supplier',views.add_supplier,name='add_supplier'),
    path('delete_supplier/<int:supplier_id>',views.delete_supplier,name="delete_supplier"),
    path('edit_supplier/<int:supplier_id>',views.edit_supplier,name="edit_supplier"),

    #Customer Path 
    path('customers',views.customers,name="customers"),
    path('add_customer',views.add_customer,name="add_customer"),
    path('delete_customer/<int:customer_id>',views.delete_customer,name="delete_customer"),
    path('edit_customer/<int:customer_id>',views.edit_customer,name="edit_customer"),

]
