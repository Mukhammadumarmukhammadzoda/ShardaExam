# Generated by Django 4.0.4 on 2022-05-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_result_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='unique_id',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]