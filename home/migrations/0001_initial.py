# Generated by Django 4.2 on 2024-12-02 07:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=255)),
                ('priority_level', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=255)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('index', models.IntegerField(default=0)),
            ],
        ),
    ]