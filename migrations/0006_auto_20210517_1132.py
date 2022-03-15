# Generated by Django 3.2.3 on 2021-05-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamDine', '0005_auto_20210517_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catering_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('dcategory', models.CharField(max_length=50)),
                ('dcapacity', models.CharField(max_length=50)),
                ('dicategory', models.CharField(max_length=50)),
                ('dicapacity', models.CharField(max_length=50)),
                ('tcategory', models.CharField(max_length=50)),
                ('tcapacity', models.CharField(max_length=50)),
                ('pcategory', models.CharField(max_length=50)),
                ('pcapacity', models.CharField(max_length=50)),
                ('rcategory', models.CharField(max_length=50)),
                ('rcapacity', models.CharField(max_length=50)),
                ('decategory', models.CharField(max_length=50)),
                ('decapacity', models.CharField(max_length=50)),
                ('drcategory', models.CharField(max_length=50)),
                ('drcapacity', models.CharField(max_length=50)),
                ('maincategory', models.CharField(max_length=50)),
                ('maincapacity', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Catering_order',
            },
        ),
        migrations.DeleteModel(
            name='Caterings',
        ),
    ]
