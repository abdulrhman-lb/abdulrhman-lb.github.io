# Generated by Django 3.0.7 on 2020-06-18 20:22

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
