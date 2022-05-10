# Generated by Django 4.0.4 on 2022-05-09 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logistic_company', models.CharField(max_length=50, verbose_name='Транспортная компания')),
                ('deadlines', models.DateTimeField(verbose_name='Сроки поставки')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=50, verbose_name='Вариант оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='Regularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regularity', models.CharField(max_length=50, verbose_name='Регулярность')),
            ],
        ),
        migrations.AlterField(
            model_name='lego',
            name='size',
            field=models.CharField(max_length=50, verbose_name='Размер'),
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.delivery')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.options')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('telephone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
            ],
        ),
        migrations.AddField(
            model_name='delivery',
            name='lego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.lego'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='regularity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.regularity'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shop'),
        ),
    ]