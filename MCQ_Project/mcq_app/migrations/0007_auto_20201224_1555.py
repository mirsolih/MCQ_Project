# Generated by Django 3.1.4 on 2020-12-24 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcq_app', '0006_auto_20201224_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='ans_num',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='if_ans',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='text',
        ),
        migrations.AddField(
            model_name='answer',
            name='a',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='b',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='c',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Question_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_text', models.TextField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mcq_app.category')),
            ],
        ),
    ]