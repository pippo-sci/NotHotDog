# Generated by Django 4.2 on 2023-05-21 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NotHotDogWebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.BooleanField()),
                ('conformity', models.BooleanField()),
                ('t_response', models.FloatField()),
                ('probability', models.DecimalField(decimal_places=2, max_digits=5)),
                ('error', models.FloatField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NotHotDogWebsite.doc')),
            ],
        ),
    ]
