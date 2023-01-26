from django.urls import path
from lechnerapp.views import productViews
from lechnerapp.views import materialViews
from lechnerapp.views import moldingtoolsViews
from lechnerapp.views import packagesViews
from lechnerapp.views import externalpartsViews



app_name = 'lechnerapp'
urlpatterns = [
    # product 
    path('products', productViews.products, name='products'),
    path('add_product',productViews.add_product,name="add_product"),
    path('delete_product/<int:product_id>',productViews.delete_product,name="delete_product"),
    path('edit_product/<int:user_id>',productViews.edit_product,name="edit_product"),
    path("getbarcode",productViews.getbarcode,name="getbarcode"),
    
    # product 
    path('materials', materialViews.materials, name='materials'),
    path('add_material',materialViews.add_material,name="add_material"),
    path('delete_material/<int:material_id>',materialViews.delete_material,name="delete_material"),
    path('edit_material/<int:material_id>',materialViews.edit_material,name="edit_material"),

    # product 
    path('moldingtools', moldingtoolsViews.moldingtools, name='moldingtools'),
    path('add_moldingtool',moldingtoolsViews.add_moldingtool,name="add_moldingtool"),
    path('delete_moldingtool/<int:moldingtool_id>',moldingtoolsViews.delete_moldingtool,name="delete_moldingtool"),
    path('edit_moldingtool/<int:moldingtool_id>',moldingtoolsViews.edit_moldingtool,name="edit_moldingtool"),

    # product 
    path('packages', packagesViews.packages, name='packages'),
    path('add_package',packagesViews.add_package,name="add_package"),
    path('delete_package/<int:package_id>',packagesViews.delete_package,name="delete_package"),
    path('edit_package/<int:package_id>',packagesViews.edit_package,name="edit_package"),

    # product 
    path('externalparts', externalpartsViews.externalparts, name='externalparts'),
    path('add_externalpart',externalpartsViews.add_externalpart,name="add_externalpart"),
    path('delete_externalpart/<int:part_id>',externalpartsViews.delete_externalpart,name="delete_externalpart"),
    path('edit_externalpart/<int:part_id>',externalpartsViews.edit_externalpart,name="edit_externalpart"),

]