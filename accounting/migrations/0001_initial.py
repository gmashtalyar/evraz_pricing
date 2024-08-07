# Generated by Django 5.0.3 on 2024-05-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=10)),
                ('document', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('sklad', models.CharField(max_length=250)),
                ('contract', models.CharField(max_length=250)),
                ('counterparty', models.CharField(max_length=250)),
                ('value', models.BigIntegerField()),
            ],
        ),
    ]
