# Generated by Django 3.0.7 on 2020-06-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20200619_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.CharField(choices=[('دمشق', 'دمشق'), ('ريف دمشق', 'ريف دمشق'), ('حلب', 'حلب'), ('حماة', 'حماة'), ('حمص', 'حمص'), ('اللاذقية', 'اللاذقية'), ('طرطوس', 'طرطوس'), ('درعا', 'درعا'), ('السويداء', 'السويداء'), ('القنيطرة', 'القنيطرة'), ('دير الزور', 'دير الزور'), ('الحسكة', 'الحسكة'), ('الرقة', 'الرقة'), ('ادلب', 'ادلب')], default='حماة', max_length=50, verbose_name='الفرع'),
        ),
    ]