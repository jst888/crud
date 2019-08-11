# Generated by Django 2.2.4 on 2019-08-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(max_length=100)),
                ('DOB', models.DateTimeField()),
                ('Mobile', models.IntegerField(null=True)),
                ('Gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Customer_No', models.IntegerField(null=True)),
                ('Country_of_Birth', models.CharField(max_length=100)),
                ('Country_of_Residence', models.CharField(max_length=100)),
                ('Customer_Segment', models.CharField(max_length=100)),
                ('Address_Type', models.CharField(blank=True, choices=[('R', 'Residence'), ('O', 'Office')], max_length=1)),
                ('Addr_line1', models.CharField(max_length=100)),
                ('Addr_line2', models.CharField(max_length=100)),
                ('Addr_line3', models.CharField(max_length=100)),
                ('Addr_line4', models.CharField(max_length=100)),
                ('Zipcode', models.IntegerField(null=True)),
                ('State', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
            ],
        ),
    ]
