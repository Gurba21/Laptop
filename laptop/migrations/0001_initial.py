# Generated by Django 3.2.9 on 2021-11-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(choices=[(1, 'Grey'), (2, 'Silver'), (3, 'Black'), (4, 'Red'), (4, 'Blue')], max_length=200)),
                ('vin', models.IntegerField()),
                ('brand', models.CharField(choices=[(1, 'Apple'), (2, 'Asus'), (3, 'Dell'), (4, 'Lenovo'), (5, 'Acer')], max_length=200)),
                ('cpu', models.CharField(max_length=200)),
                ('ram', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('display', models.CharField(choices=[(1, '4096 x 2160'), (2, '2048 x 1080'), (3, '1920 x 1080'), (4, '1024 x 768')], max_length=200)),
                ('battery', models.IntegerField()),
                ('prod', models.CharField(max_length=200)),
            ],
        ),
    ]
