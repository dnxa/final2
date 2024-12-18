# Generated by Django 5.1.4 on 2024-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Santa_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santaslist',
            name='naughty_list',
            field=models.ManyToManyField(blank=True, related_name='naughty_lists', to='Santa_list.kid'),
        ),
        migrations.AlterField(
            model_name='santaslist',
            name='nice_list',
            field=models.ManyToManyField(blank=True, related_name='nice_list', to='Santa_list.kid'),
        ),
    ]