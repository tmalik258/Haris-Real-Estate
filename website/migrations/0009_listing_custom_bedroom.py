# Generated by Django 4.1.7 on 2023-04-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_profile_bio_info_alter_profile_estate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='custom_bedroom',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
