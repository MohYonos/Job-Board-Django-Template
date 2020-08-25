# Generated by Django 3.1 on 2020-08-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experinces',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('FULL TIME', 'FULL TIME'), ('PART TIME', 'PART TIME'), ('FREELANCER', 'FREELANCER')], default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]