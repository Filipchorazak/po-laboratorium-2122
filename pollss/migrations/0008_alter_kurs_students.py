# Generated by Django 4.0.4 on 2022-05-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollss', '0007_rename_enrollment_zapisy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurs',
            name='students',
            field=models.ManyToManyField(through='pollss.Zapisy', to='pollss.student'),
        ),
    ]
