# Generated by Django 2.0 on 2018-07-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('araba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='araba',
            name='modeli',
            field=models.IntegerField(default=2018),
        ),
        migrations.AlterField(
            model_name='araba',
            name='arabaismi',
            field=models.CharField(max_length=120, verbose_name='ARAÇ ADI'),
        ),
        migrations.AlterField(
            model_name='araba',
            name='ilantarihi',
            field=models.DateTimeField(verbose_name='iLAN TARİHİ'),
        ),
        migrations.AlterField(
            model_name='araba',
            name='ozellikler',
            field=models.TextField(verbose_name='ÖZELLİKLER'),
        ),
    ]
