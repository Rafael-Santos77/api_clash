# Generated by Django 4.2.5 on 2023-10-01 20:29

import clash.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clash', '0005_alter_heroina_options_alter_king_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatarheroes',
            fields=[
                ('nome_img', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=clash.models.img)),
            ],
        ),
    ]
