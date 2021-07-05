# Generated by Django 3.2 on 2021-07-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.CharField(max_length=100)),
                ('row_size', models.IntegerField(default=0)),
                ('column_size', models.IntegerField(default=0)),
            ],
        ),
    ]
