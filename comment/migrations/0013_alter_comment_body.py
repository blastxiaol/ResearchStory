# Generated by Django 3.2.4 on 2021-07-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(),
        ),
    ]