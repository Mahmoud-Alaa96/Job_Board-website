# Generated by Django 4.1.7 on 2023-02-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
