# Generated by Django 4.0.6 on 2022-07-16 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nhanvien', '0003_remove_quanlynhanvien_namsinhnv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quanlynhanvien',
            old_name='chucvunv',
            new_name='ho',
        ),
    ]