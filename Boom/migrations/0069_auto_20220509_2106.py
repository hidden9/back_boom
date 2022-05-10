# Generated by Django 3.2.12 on 2022-05-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boom', '0068_alter_artwork_advertisement_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork_advertisement',
            name='Hipe',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='image_1',
            field=models.ImageField(null=True, upload_to='Boom/media'),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='image_2',
            field=models.ImageField(null=True, upload_to='Boom/media'),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='image_3',
            field=models.ImageField(null=True, upload_to='Boom/media'),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='image_4',
            field=models.ImageField(null=True, upload_to='Boom/media'),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='image_5',
            field=models.ImageField(null=True, upload_to='Boom/media'),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='status',
            field=models.CharField(choices=[('sold', 'sold'), ('available', 'available')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='style',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
