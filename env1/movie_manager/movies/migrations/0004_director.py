# Generated by Django 4.2.6 on 2023-10-25 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_delete_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]