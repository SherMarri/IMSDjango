# Generated by Django 2.0.1 on 2018-01-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('contact', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]