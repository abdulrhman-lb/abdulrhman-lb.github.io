# Generated by Django 3.0.7 on 2020-06-18 23:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200618_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10)], verbose_name='جوال'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nation_num',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(11), django.core.validators.MaxValueValidator(11)], verbose_name='الرقم الوطني'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10)], verbose_name='الهاتف'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_branch',
            field=models.CharField(choices=[('شعبة السلمية', 'شعبة السلمية'), ('شعبة مصياف', 'شعبة مصياف'), ('شعبة السقيلبية', 'شعبة السقيلبية'), ('فرع حماة', 'فرع حماة')], max_length=50, verbose_name='الشعبة'),
        ),
    ]
