# Generated by Django 4.0.6 on 2022-07-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quanlynhanvien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tennv', models.CharField(max_length=100)),
                ('chucvunv', models.CharField(max_length=100)),
                ('namsinhnv', models.IntegerField(max_length=100)),
            ],
        ),
    ]