# Generated by Django 5.2.1 on 2025-06-25 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearnapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='otp_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course_details',
            name='course_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='s_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='s_qualification',
            field=models.CharField(max_length=50),
        ),
    ]
