# Generated by Django 3.2 on 2022-01-07 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('recipient_city', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Chennai', 'Chennai'), ('Bangalore', 'Bangalore'), ('Kolkata', 'Kolkata')], max_length=100)),
                ('sending_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
