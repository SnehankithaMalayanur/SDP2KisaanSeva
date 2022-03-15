# Generated by Django 3.2.3 on 2021-05-17 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DreamDine', '0009_corder'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_cater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cater_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DreamDine.cater')),
            ],
            options={
                'db_table': 'order_cater',
            },
        ),
        migrations.DeleteModel(
            name='COrder',
        ),
    ]
