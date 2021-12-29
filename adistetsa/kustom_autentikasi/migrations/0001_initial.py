# Generated by Django 4.0 on 2021-12-28 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataprofil', '0010_delete_datasiswauser'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSiswaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NISN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprofil.datasiswa')),
                ('USER', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
