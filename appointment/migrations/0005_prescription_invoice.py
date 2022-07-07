# Generated by Django 4.0.3 on 2022-05-06 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_dailyslotbooking_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('symptoms', models.CharField(max_length=200)),
                ('prescription_date', models.DateField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_fee', models.PositiveIntegerField()),
                ('medicine_charges', models.PositiveIntegerField()),
                ('lab_fee', models.PositiveIntegerField()),
                ('other_charges', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField()),
                ('paid_amount', models.PositiveIntegerField()),
                ('due_amount', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
            ],
        ),
    ]