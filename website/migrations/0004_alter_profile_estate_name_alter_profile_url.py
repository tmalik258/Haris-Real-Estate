# Generated by Django 4.1.3 on 2023-03-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_profile_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='estate_name',
            field=models.CharField(default='Haris Real Estate', max_length=256),
        ),
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True, verbose_name='HarisRealEstateProfile'),
        ),
    ]
