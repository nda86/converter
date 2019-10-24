# Generated by Django 2.2.6 on 2019-10-23 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate', models.FloatField()),
                ('volume', models.FloatField()),
                ('currency_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Currency')),
            ],
        ),
    ]