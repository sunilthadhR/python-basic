# Generated by Django 4.2.15 on 2024-09-16 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_rename_bonuses_payroll_pf'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('earned', 'Earned Leave')], max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.user')),
            ],
        ),
    ]
