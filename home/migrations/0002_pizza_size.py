# Generated by Django 5.1.7 on 2025-04-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='medium', max_length=10),
        ),
    ]
