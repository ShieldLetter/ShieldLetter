# Generated by Django 3.2.19 on 2023-12-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shieldletter', '0004_alter_board_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='file',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='board',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
