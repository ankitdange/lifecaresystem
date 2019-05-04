# Generated by Django 2.1.2 on 2019-04-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(choices=[('MBBS( Bachelor of Medicine, Bachelor of Surgery)', 'MBBS( Bachelor of Medicine, Bachelor of Surgery)'), ('BDS', 'BDS(Bachelor of Dental Surgery)'), ('BAMS', 'BAMS( Bachelor of Ayurvedic Medicine and Surgery)'), ('BUMS', 'BUMS(Bachelor of Unani Medicine and Surgery)'), ('BHMS ', 'BHMS( Bachelor of Homeopathy Medicine and Surgery)'), ('MD', 'MD(Doctor of Medicine)'), ('MS', 'MS(Masters of Surgery)'), ('DNB', 'DNB(Diplomate of National Board )')], max_length=8),
        ),
    ]