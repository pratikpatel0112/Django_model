# Generated by Django 4.1.1 on 2022-09-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('Student_name', models.CharField(max_length=50)),
                ('student_email', models.CharField(max_length=50)),
                ('student_fees', models.FloatField(default=10000)),
            ],
        ),
    ]
