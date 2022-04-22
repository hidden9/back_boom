# Generated by Django 3.2.12 on 2022-04-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boom', '0056_auto_20220414_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='Experience_in_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='artfield',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='stylework',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('sold', 'sold')], max_length=200, null=True),
        ),
    ]
