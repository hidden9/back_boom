# Generated by Django 4.0.3 on 2022-04-02 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boom', '0013_remove_artist_free_post_artwork_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='artwork_advertisement',
            name='createAt',
        ),
    ]