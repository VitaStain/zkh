# Generated by Django 4.2.1 on 2023-05-19 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("workers", "0001_initial"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="worker",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order",
                to="workers.worker",
            ),
        ),
    ]
