# Generated by Django 3.0.8 on 2021-01-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
