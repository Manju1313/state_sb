# Generated by Django 4.1.3 on 2022-12-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_data_remove_person_city_remove_person_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
