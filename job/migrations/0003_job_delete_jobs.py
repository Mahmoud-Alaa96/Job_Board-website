# Generated by Django 4.1.7 on 2023-02-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_rename_job_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]