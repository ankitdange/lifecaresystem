# Generated by Django 2.1.2 on 2019-04-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescribed_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmedicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Patient_appointment')),
            ],
        ),
    ]
