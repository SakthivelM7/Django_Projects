# Generated by Django 4.2.6 on 2023-11-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('Fname', models.CharField(max_length=150)),
                ('Lname', models.CharField(max_length=150)),
                ('Phno', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.IntegerField()),
                ('mov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.movie')),
                ('theater_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.theater')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_of_seats', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.customer')),
                ('mov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.movie')),
            ],
        ),
    ]
