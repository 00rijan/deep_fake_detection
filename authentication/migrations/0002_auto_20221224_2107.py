# Generated by Django 3.0.5 on 2022-12-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='confidence',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='history',
            name='sequence',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
