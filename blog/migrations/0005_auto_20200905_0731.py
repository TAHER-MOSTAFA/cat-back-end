# Generated by Django 3.0.5 on 2020-09-05 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_comments_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auther',
            new_name='author',
        ),
    ]
