from django.db import models

class Crud(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    ADDRESS_TYPE = [('R', 'Residence'), ('O', 'Office')]
    First_Name = models.CharField(null=True, max_length=100)
    Middle_Name = models.CharField(null=True, max_length=100)
    Last_Name = models.CharField(null=True, max_length=100)
    DOB = models.DateField(null=True, blank=True)
    Mobile = models.IntegerField(null=True)
    Gender = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    Customer_No = models.IntegerField(null=True)
    Country_of_Birth = models.CharField(max_length=100)
    Country_of_Residence = models.CharField(max_length=100)
    Customer_Segment = models.CharField(max_length=100)
    Address_Type = models.CharField(choices=ADDRESS_TYPE, max_length=1, blank=True)
    Addr_line1 = models.CharField(max_length=100, blank=True)
    Addr_line2 = models.CharField(max_length=100, blank=True)
    Addr_line3 = models.CharField(max_length=100, blank=True)
    Addr_line4 = models.CharField(max_length=100, blank=True)
    Zipcode = models.IntegerField(null=True)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
