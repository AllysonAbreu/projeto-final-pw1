# Generated by Django 3.2.7 on 2021-09-16 20:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import localflavor.br.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('cpf', localflavor.br.models.BRCPFField(max_length=14, verbose_name='CPF')),
                ('name', models.CharField(max_length=250, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', localflavor.br.models.BRPostalCodeField(max_length=9, verbose_name='CEP')),
                ('address', models.CharField(max_length=250, verbose_name='Endereço')),
                ('number', models.CharField(max_length=250, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=250, verbose_name='Complemento')),
                ('district', models.CharField(max_length=250, verbose_name='Bairro')),
                ('state', localflavor.br.models.BRStateField(max_length=2, verbose_name='Estado')),
                ('city', models.CharField(max_length=250, verbose_name='Cidade')),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product')),
            ],
        ),
    ]
