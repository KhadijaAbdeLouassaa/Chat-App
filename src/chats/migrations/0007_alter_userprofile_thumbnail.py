# Generated by Django 4.2.16 on 2024-09-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_alter_userprofile_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='thumbnail',
            field=models.ImageField(default='images\\default_thumbnail.png', upload_to='users_thumbnail'),
        ),
    ]