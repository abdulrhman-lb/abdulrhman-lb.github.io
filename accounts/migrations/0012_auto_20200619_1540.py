# Generated by Django 3.0.7 on 2020-06-19 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200619_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blood_type',
            field=models.CharField(choices=[('A-', 'A-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('A+', 'A+'), ('B-', 'B-')], max_length=50, verbose_name='زمرة الدم'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('شهادة جامعية', 'شهادة جامعية'), ('شهادة ثانوية', 'شهادة ثانوية'), ('شهادة إعدادية', 'شهادة إعدادية'), ('دكتوراه', 'دكتوراه'), ('شهادة ابتدائية', 'شهادة ابتدائية'), ('طالب جامعي', 'طالب جامعي'), ('معهد', 'معهد'), ('دبلوم', 'دبلوم'), ('ماجستير', 'ماجستير'), ('غير متعلم', 'غير متعلم')], max_length=50, verbose_name='الشهادة العلمية '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nation_num',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('[0-9].{11}$')], verbose_name='الرقم الوطني'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('سائق', 'سائق'), ('منسق التدريب', 'منسق التدريب'), ('مسؤول مركز', 'مسؤول مركز'), ('مستخدم', 'مستخدم'), ('منسق عمليات الإسعاف', 'منسق عمليات الإسعاف'), ('لوجستي إسعاف', 'لوجستي إسعاف'), ('مساعد منسق الإسعاف', 'مساعد منسق الإسعاف'), ('مستشار طبي', 'مستشار طبي'), ('منسق فريق الإسعاف', 'منسق فريق الإسعاف')], max_length=50, verbose_name='المنصب'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position_e',
            field=models.CharField(choices=[('Medical Advisor', 'Medical Advisor'), ('user', 'user'), ('Ambulance Logistic', 'Ambulance Logistic'), ('Training Coordinator', 'Training Coordinator'), ('Driver', 'Driver'), ('Center Official', 'Center Official'), ('Assistant Ambulance Coordinator', 'Assistant Ambulance Coordinator'), ('Ambulance Operations Coordinator', 'Ambulance Operations Coordinator'), ('Ambulance Team Coordinator', 'Ambulance Team Coordinator')], max_length=50, verbose_name='المنصب بالانكليزي'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank_in_team',
            field=models.CharField(choices=[('كشاف', 'كشاف'), ('مسعف تحت التدريب', 'مسعف تحت التدريب'), ('قائد فريق', 'قائد فريق'), ('قائد قطاع', 'قائد قطاع'), ('قائد قطاع تحت التدريب', 'قائد قطاع تحت التدريب'), ('مسعف', 'مسعف')], max_length=50, verbose_name='الرتبة ضمن الفريق'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sarc_adjective',
            field=models.CharField(choices=[('موظف', 'موظف'), ('متطوع', 'متطوع')], max_length=50, verbose_name='الصفة الهلالية'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shoulder_size',
            field=models.CharField(choices=[('XXL', 'XXL'), ('L', 'L'), ('XL', 'XL'), ('M', 'M'), ('S', 'S')], max_length=50, verbose_name='قياس الكتفين'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sub_branch',
            field=models.CharField(choices=[('شعبة مصياف', 'شعبة مصياف'), ('فرع حماة', 'فرع حماة'), ('شعبة السقيلبية', 'شعبة السقيلبية'), ('شعبة السلمية', 'شعبة السلمية')], max_length=50, verbose_name='الشعبة'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='training_postion',
            field=models.CharField(choices=[('مساعد مدرب', 'مساعد مدرب'), ('مدرب', 'مدرب')], max_length=50, verbose_name='الصفة بالتدريب'),
        ),
    ]