# Generated by Django 2.0 on 2018-07-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('araba', '0002_auto_20180702_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='araba',
            name='foto1',
            field=models.ImageField(blank='True', null='True', upload_to=''),
        ),
        migrations.AlterField(
            model_name='araba',
            name='ilantarihi',
            field=models.DateTimeField(auto_now_add=True, verbose_name='iLAN TARİHİ'),
        ),
    ]