# Generated by Django 3.0.7 on 2020-06-19 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200619_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('طالب جامعي', 'طالب جامعي'), ('معهد', 'معهد'), ('دكتوراه', 'دكتوراه'), ('شهادة ابتدائية', 'شهادة ابتدائية'), ('شهادة ثانوية', 'شهادة ثانوية'), ('غير متعلم', 'غير متعلم'), ('ماجستير', 'ماجستير'), ('دبلوم', 'دبلوم'), ('شهادة جامعية', 'شهادة جامعية'), ('شهادة إعدادية', 'شهادة إعدادية')], max_length=50, verbose_name='الشهادة العلمية '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)], verbose_name='جوال'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nation_num',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10000000000), django.core.validators.MaxValueValidator(99999999999)], verbose_name='الرقم الوطني'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)], verbose_name='الهاتف'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='point',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='النقطة'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_status',
            field=models.CharField(choices=[('أعزب', 'أعزب'), ('متزوج', 'متزوج')], max_length=50, verbose_name='الحالة الاجتماعية'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_branch',
            field=models.CharField(choices=[('شعبة السلمية', 'شعبة السلمية'), ('شعبة السقيلبية', 'شعبة السقيلبية'), ('شعبة مصياف', 'شعبة مصياف'), ('فرع حماة', 'فرع حماة')], max_length=50, verbose_name='الشعبة'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_person',
            field=models.CharField(choices=[('أنثى', 'أنثى'), ('ذكر', 'ذكر')], max_length=50, verbose_name='  الجنس'),
        ),
    ]