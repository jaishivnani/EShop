# Generated by Django 3.1.2 on 2020-11-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=5000)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
