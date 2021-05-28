# Generated by Django 2.2 on 2021-03-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='author',
            name='personal_page',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='author',
            name='second_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='university',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
