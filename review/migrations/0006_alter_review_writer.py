# Generated by Django 4.2.4 on 2023-08-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='writer',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
