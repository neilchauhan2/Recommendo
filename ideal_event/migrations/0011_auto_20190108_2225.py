# Generated by Django 2.1.5 on 2019-01-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideal_event', '0010_auto_20190108_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='interest2',
            name='interest_name',
        ),
        migrations.RemoveField(
            model_name='interest3',
            name='interest_x',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Interest2',
        ),
        migrations.DeleteModel(
            name='Interest3',
        ),
    ]
