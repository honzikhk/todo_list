# Generated by Django 4.0.5 on 2022-06-18 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_task_dead_line_time_alter_task_to_do_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed', '-dead_line']},
        ),
    ]