# Generated by Django 4.2.2 on 2023-09-12 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poststable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poststable.author'),
        ),
    ]