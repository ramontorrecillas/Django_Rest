# Generated by Django 3.0.6 on 2020-05-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postalcodes',
            fields=[
                ('idpostalcode', models.AutoField(db_column='idPostalCode', primary_key=True, serialize=False)),
                ('holidays', models.TextField(db_column='holidays')),
                ('audtimestamp', models.TextField(blank=True, db_column='audTimestamp', null=True)),
            ],
            options={
                'db_table': 'PostalCodes',
                'managed': False,
            },
        ),
    ]
