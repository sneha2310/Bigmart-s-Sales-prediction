from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
        list_display = ('Item_Identifier', 'Item_Weight', 'Item_Fat_Content', 'Item_Type', 'Item_MRP', 'Outlet_Identifier', 'Outlet_Location_Type', 'Outlet_Type')
        pass
