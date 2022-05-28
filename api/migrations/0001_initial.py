# Generated by Django 4.0.4 on 2022-05-28 17:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.UUIDField(help_text='Identificación del usuario')),
                ('user_alternate_id', models.CharField(max_length=50, verbose_name='Identificacion usuario no registrado')),
                ('delivery_id', models.UUIDField(help_text='Identificación del usuario')),
                ('total_value', models.IntegerField(help_text='Total a pagar')),
                ('is_active', models.BooleanField(default=False, help_text='Envío aprovado')),
                ('paid', models.BooleanField(default=False, help_text='Pago')),
                ('rating', models.IntegerField(choices=[(5, 'Excelent'), (4, 'Good'), (3, 'Regular'), (2, 'Mediocre'), (1, 'Forget Me')], default=5, help_text='Calificación del servicio')),
                ('order_list', models.JSONField(help_text='Pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nombre', max_length=50, unique=True)),
                ('description', models.CharField(blank=True, help_text='Descripción', max_length=250)),
                ('image', models.FileField(help_text='Imagen del producto', upload_to='assets')),
                ('price', models.IntegerField(default=0, help_text='Valor del producto')),
                ('qualification', models.IntegerField(choices=[(5, 'Excelent'), (4, 'Yum'), (3, 'Regular'), (2, 'Yuk'), (1, 'Ugh')], default=5, help_text='Calificación del producto')),
                ('reviewers', models.IntegerField(default=0, help_text='Cantidad de reviews')),
                ('category', models.IntegerField(choices=[(0, 'None'), (1, 'Hamburguer'), (2, 'Pizza'), (3, 'Taco'), (4, 'Drink')], default=0, help_text='Categoría')),
                ('visible', models.BooleanField(default=True, help_text='Visible en el menu')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Lastname')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
