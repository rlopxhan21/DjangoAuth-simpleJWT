# Generated by Django 4.1.5 on 2023-02-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]