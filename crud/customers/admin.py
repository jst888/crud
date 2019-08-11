from django.contrib import admin

from .models import Crud

@admin.register(Crud)
class CrudAdmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Middle_Name', 'Last_Name', 'DOB', 'Mobile', 'Gender', 'Customer_No', 'Country_of_Birth','Country_of_Residence', 'Customer_Segment', 'Address_Type', 'Addr_line1', 'Addr_line2','Addr_line3','Addr_line4', 'Zipcode', 'State','City']

