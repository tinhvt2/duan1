# Generated by Django 4.0.6 on 2022-07-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhanvien', '0005_rename_ho_quanlynhanvien_chucvunv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quanlynhanvien',
            old_name='chucvunv',
            new_name='chucvu_nv',
        ),
        migrations.RenameField(
            model_name='quanlynhanvien',
            old_name='namsinhnv',
            new_name='namsinh_nv',
        ),
        migrations.RenameField(
            model_name='quanlynhanvien',
            old_name='tennv',
            new_name='ten_nv',
        ),
    ]
