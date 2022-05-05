# Generated by Django 4.0.4 on 2022-05-04 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creatures', '0004_dispel_type_school_ability_creature_abilities'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dispel_Type',
            new_name='DispelType',
        ),
        migrations.AlterModelOptions(
            name='ability',
            options={'verbose_name': 'ability', 'verbose_name_plural': 'abilities'},
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'class', 'verbose_name_plural': 'classes'},
        ),
        migrations.AlterField(
            model_name='ability',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='creatures.school'),
        ),
    ]
