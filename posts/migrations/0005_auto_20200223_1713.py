# Generated by Django 2.2 on 2020-02-23 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_likecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-posted_at',)},
        ),
    ]