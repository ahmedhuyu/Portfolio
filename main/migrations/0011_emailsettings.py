# Generated by Django 5.2.2 on 2025-06-06 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_work_works_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_host_user', models.EmailField(max_length=254, verbose_name='Email Host User')),
                ('email_host_password', models.CharField(max_length=255, verbose_name='Email Host Password')),
            ],
            options={
                'verbose_name': 'Email Settings',
                'verbose_name_plural': 'Email Settings',
            },
        ),
    ]
