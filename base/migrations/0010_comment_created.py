# Generated by Django 4.0.5 on 2022-06-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
