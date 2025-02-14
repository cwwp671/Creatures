# Generated by Django 4.0.4 on 2022-05-04 22:49

import creatures.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creatures', '0002_classification_expansion_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('model_image', models.ImageField(upload_to=creatures.models.model_image_path)),
                ('type', models.CharField(max_length=128)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatures', to='creatures.classification')),
                ('creature_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatures', to='creatures.class')),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatures', to='creatures.faction')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatures', to='creatures.level')),
            ],
        ),
    ]
