# Generated by Django 5.0.6 on 2024-11-21 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lamoda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LamodaShapka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_lamoda.category')),
            ],
        ),
    ]
