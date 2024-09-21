# Generated by Django 5.0.1 on 2024-09-21 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='ajust_app.event')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='ajust_app.event')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.CharField(choices=[('YES', '◯'), ('NO', '✕'), ('MAYBE', '△')], max_length=5)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='ajust_app.date')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='ajust_app.participant')),
            ],
        ),
    ]
