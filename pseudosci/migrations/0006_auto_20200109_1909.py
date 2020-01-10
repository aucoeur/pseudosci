# Generated by Django 3.0.2 on 2020-01-10 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pseudosci', '0005_remove_choice_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='result',
        ),
        migrations.AddField(
            model_name='choice',
            name='result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pseudosci.Result'),
        ),
    ]
