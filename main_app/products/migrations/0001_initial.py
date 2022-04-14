# Generated by Django 3.2.5 on 2022-04-13 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(choices=[('g', 'gram'), ('Kcal', 'kcal')], max_length=5)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddConstraint(
            model_name='nutrition',
            constraint=models.UniqueConstraint(fields=('name', 'product'), name='unique_nutrition_product'),
        ),
    ]
