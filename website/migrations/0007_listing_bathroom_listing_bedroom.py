# Generated by Django 4.1.3 on 2023-03-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_user_estate_name_alter_user_bio_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathroom',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6)], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='listing',
            name='bedroom',
            field=models.CharField(choices=[('S', 'Studio'), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default='', max_length=6),
        ),
    ]
