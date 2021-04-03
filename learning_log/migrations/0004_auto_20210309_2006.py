# Generated by Django 3.1.7 on 2021-03-09 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0003_auto_20210220_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='Topic',
        ),
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='learning_log.topic'),
        ),
    ]