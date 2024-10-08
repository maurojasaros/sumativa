# Generated by Django 5.1 on 2024-09-14 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0002_categoria_juego_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.carrito')),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.juego')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('carrito', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='juegos.carrito')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('direccion', models.TextField()),
                ('tipo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='juegos.tipousuario')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='juegos.usuario'),
        ),
    ]
