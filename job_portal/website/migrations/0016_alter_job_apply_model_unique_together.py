# Generated by Django 4.0.4 on 2022-05-15 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_job_apply_model_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job_apply_model',
            unique_together={('job_company_email', 'job_seeker_email', 'job_title')},
        ),
    ]