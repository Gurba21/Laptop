# Generated by Django 3.2.9 on 2021-11-12 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laptop', '0003_auto_20211110_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='battery',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='memory',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='vin',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
