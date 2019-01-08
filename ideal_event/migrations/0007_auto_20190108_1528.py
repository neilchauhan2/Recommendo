# Generated by Django 2.1.5 on 2019-01-08 15:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideal_event', '0006_auto_20190108_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_level', models.DecimalField(decimal_places=1, default=0, max_digits=6, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.0)])),
                ('interest_x', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ideal_event.Interest2')),
            ],
        ),
        migrations.RemoveField(
            model_name='interest',
            name='interest_level',
        ),
    ]
