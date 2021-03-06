# Generated by Django 4.0 on 2021-12-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataprofil', '0006_alter_dataorangtua_data_anak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataorangtua',
            name='JENJANG_PENDIDIKAN_AYAH',
            field=models.CharField(choices=[('Tidak Bersekolah', 'Tidak Bersekolah'), ('SD/Sederajat', 'SD/Sederajat'), ('SMP/Sederajat', 'SMP/Sederajat'), ('SMA/Sederajat', 'SMA/Sederajat'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('Lainnya', 'Lainnya')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dataorangtua',
            name='JENJANG_PENDIDIKAN_IBU',
            field=models.CharField(choices=[('Tidak Bersekolah', 'Tidak Bersekolah'), ('SD/Sederajat', 'SD/Sederajat'), ('SMP/Sederajat', 'SMP/Sederajat'), ('SMA/Sederajat', 'SMA/Sederajat'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('Lainnya', 'Lainnya')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dataorangtua',
            name='JENJANG_PENDIDIKAN_WALI',
            field=models.CharField(choices=[('Tidak Bersekolah', 'Tidak Bersekolah'), ('SD/Sederajat', 'SD/Sederajat'), ('SMP/Sederajat', 'SMP/Sederajat'), ('SMA/Sederajat', 'SMA/Sederajat'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('Lainnya', 'Lainnya')], max_length=20),
        ),
    ]
