# Generated by Django 3.2 on 2022-12-21 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='artists.artist')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Song',
            },
        ),
    ]
