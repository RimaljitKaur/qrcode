# Generated by Django 4.2 on 2023-04-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_code_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='qr_code',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
