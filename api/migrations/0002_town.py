# Generated by Django 2.2.5 on 2019-09-16 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the town', max_length=50)),
                ('province', models.ForeignKey(help_text='Towns in the province', on_delete=django.db.models.deletion.CASCADE, related_name='towns', to='api.Province')),
            ],
        ),
    ]
