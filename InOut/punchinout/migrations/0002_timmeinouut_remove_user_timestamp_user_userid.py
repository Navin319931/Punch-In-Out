# Generated by Django 4.1.1 on 2022-09-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punchinout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='timmeinouut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50, null=True, verbose_name='Userid')),
                ('timestamp', models.DateTimeField(verbose_name='Time and date')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=50, null=True, verbose_name='Userid'),
        ),
    ]
