# Generated by Django 4.2.16 on 2024-11-14 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_alter_staf_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'default_permissions': 'view', 'permissions': (('add_dish', 'Can add dish'), ('change_dish', 'Can change dish'), ('del_dish', 'Can del dish'))},
        ),
    ]
