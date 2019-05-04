# Generated by Django 2.1.7 on 2019-03-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_Pregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
        ),
    ]
