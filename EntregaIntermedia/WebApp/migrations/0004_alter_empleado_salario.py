# Generated by Django 4.0.6 on 2022-08-02 23:23

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_cliente_foto_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='salario',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('1'), default_currency='USD', max_digits=11),
        ),
    ]
