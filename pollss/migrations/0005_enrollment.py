# Generated by Django 4.0.4 on 2022-05-25 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollss', '0004_student_kurs'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField()),
                ('final_grade', models.CharField(blank=True, max_length=1, null=True)),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollss.kurs')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollss.student')),
            ],
        ),
    ]
