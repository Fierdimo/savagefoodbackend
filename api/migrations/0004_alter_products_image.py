# Generated by Django 4.0.4 on 2022-05-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_products_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.FileField(help_text='Imagen del producto', upload_to='assets'),
        ),
    ]
