# Generated by Django 4.0.4 on 2022-05-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_jobs_model_job_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_apply_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_company_email', models.EmailField(max_length=50)),
                ('job_seeker_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobseeker_model',
            name='applied_company',
        ),
        migrations.RemoveField(
            model_name='jobseeker_model',
            name='applied_job',
        ),
    ]
