# Generated by Django 3.2 on 2023-07-15 15:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mathematical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='equation',
            name='solution_id',
            field=models.UUIDField(null=True),
        ),
    ]
