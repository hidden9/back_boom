# Generated by Django 3.2.12 on 2022-04-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boom', '0052_alter_artist_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]