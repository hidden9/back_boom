# Generated by Django 4.0.3 on 2022-05-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boom', '0003_artwork_advertisement_admin_perm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='status',
            field=models.CharField(choices=[('sold', 'sold'), ('available', 'available')], max_length=200, null=True),
        ),
    ]
