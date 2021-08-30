# Generated by Django 3.1.4 on 2021-01-25 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcq_app', '0010_auto_20210106_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mcq_app.template')),
            ],
        ),
    ]