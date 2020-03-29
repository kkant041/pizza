# Generated by Django 3.0.3 on 2020-03-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dinner_platters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platter_name', models.CharField(max_length=100)),
                ('platter_small_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('platter_large_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'dinner_platters',
                'verbose_name_plural': 'dinner_platterss',
            },
        ),
        migrations.CreateModel(
            name='pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta_name', models.CharField(max_length=100)),
                ('pasta_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'pasta',
                'verbose_name_plural': 'pastas',
            },
        ),
        migrations.CreateModel(
            name='salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salads_name', models.CharField(max_length=100)),
                ('salads_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'salads',
                'verbose_name_plural': 'saladss',
            },
        ),
        migrations.CreateModel(
            name='sicilianpizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sic_pizza', models.CharField(max_length=100)),
                ('sic_small_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sic_large_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'sicilianpizza',
                'verbose_name_plural': 'sicilianpizzas',
            },
        ),
        migrations.CreateModel(
            name='subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs_name', models.CharField(max_length=100)),
                ('sub_small_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sub_large_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'subs',
                'verbose_name_plural': 'subss',
            },
        ),
        migrations.CreateModel(
            name='toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'toppings',
                'verbose_name_plural': 'toppingss',
            },
        ),
    ]
