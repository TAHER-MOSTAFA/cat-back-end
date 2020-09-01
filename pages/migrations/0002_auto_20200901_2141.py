# Generated by Django 3.0.5 on 2020-09-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='git',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='linked_in',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('leader', 'leader'), ('mentor', 'mentor'), ('member', 'member'), ('cor', 'cor')], max_length=10),
        ),
    ]
