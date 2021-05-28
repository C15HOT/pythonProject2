# Generated by Django 2.2 on 2021-03-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20210331_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('r', 'Review'), ('p', 'Published')], default='d', max_length=1),
        ),
    ]