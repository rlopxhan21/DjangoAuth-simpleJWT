# Generated by Django 4.1.5 on 2023-02-02 00:55

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0004_alter_user_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profileImage',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='users/pp.jpg', force_format='JPEG', keep_meta=True, null=True, quality=75, scale=None, size=[500, 500], upload_to='users/'),
        ),
    ]
