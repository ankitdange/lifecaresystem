# Generated by Django 2.1.2 on 2019-04-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_Labtechnician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('1', 'BMLT'), ('2', 'DMLT'), ('3', 'CMLT'), ('4', 'Bsc(MLT)')], max_length=4)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Add_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(max_length=50)),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
