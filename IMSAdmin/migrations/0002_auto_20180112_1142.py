# Generated by Django 2.0.1 on 2018-01-12 11:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('IMSAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPolicyComprehensive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('effectiveFrom', models.DateField()),
                ('effectiveTill', models.DateField()),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
                ('totalAmount', models.FloatField()),
                ('commission', models.FloatField()),
                ('policyType', models.BooleanField()),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('repairType', models.BooleanField()),
                ('premium', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerPolicyTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('effectiveFrom', models.DateField()),
                ('effectiveTill', models.DateField()),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
                ('totalAmount', models.FloatField()),
                ('commission', models.FloatField()),
                ('policyType', models.BooleanField()),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fixedValue', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PolicyComprehensive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('repairType', models.BooleanField()),
                ('minVehicle', models.FloatField()),
                ('maxVehicle', models.FloatField()),
                ('premium', models.FloatField()),
                ('minAmount', models.FloatField()),
                ('commission', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('insuranceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.InsuranceCompany')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PolicyTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('fixedValue', models.FloatField()),
                ('minVehicle', models.FloatField()),
                ('maxVehicle', models.FloatField()),
                ('commission', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('insuranceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.InsuranceCompany')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.VehicleMake')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('value', models.FloatField()),
                ('year', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.VehicleModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='AdminProfile',
        ),
        migrations.AddField(
            model_name='customerpolicytp',
            name='insuranceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.InsuranceCompany'),
        ),
        migrations.AddField(
            model_name='customerpolicytp',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.VehicleModel'),
        ),
        migrations.AddField(
            model_name='customerpolicycomprehensive',
            name='insuranceCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.InsuranceCompany'),
        ),
        migrations.AddField(
            model_name='customerpolicycomprehensive',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMSAdmin.VehicleModel'),
        ),
    ]
