# Generated by Django 3.2.12 on 2022-04-17 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Boom', '0058_auto_20220415_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork_advertisement',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('sold', 'sold')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Sample_artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(blank=True, max_length=200, null=True)),
                ('materials', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=200, null=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Boom.artist')),
            ],
        ),
    ]