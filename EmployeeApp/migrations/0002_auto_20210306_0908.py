# Generated by Django 3.1.7 on 2021-03-06 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empolyees',
            new_name='Employees',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmpolyeeId',
            new_name='EmployeeId',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmpolyeeName',
            new_name='EmployeeName',
        ),
    ]
