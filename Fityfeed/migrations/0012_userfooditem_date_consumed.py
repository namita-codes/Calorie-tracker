# Generated by Django 5.0.6 on 2024-07-30 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fityfeed', '0011_userfooditem_meal_type_alter_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfooditem',
            name='date_consumed',
            field=models.DateField(auto_now_add=True, default=datetime.date(2023, 1, 1)),
            preserve_default=False,
        ),
    ]
