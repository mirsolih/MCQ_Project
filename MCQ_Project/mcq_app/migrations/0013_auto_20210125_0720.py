# Generated by Django 3.1.4 on 2021-01-25 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcq_app', '0012_auto_20210125_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='cat_amount',
        ),
        migrations.AddField(
            model_name='test',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mcq_app.template'),
        ),
    ]