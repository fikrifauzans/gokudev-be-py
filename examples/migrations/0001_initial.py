# Generated by Django 5.0.6 on 2024-06-04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="example_table",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("string", models.CharField(max_length=255, null=True)),
                ("text", models.TextField(null=True)),
                ("smallint", models.SmallIntegerField(null=True)),
                ("integer", models.IntegerField(null=True)),
                ("biginteger", models.BigIntegerField(null=True)),
                ("boolean", models.BooleanField(default=False)),
                ("date", models.DateField(null=True)),
                ("datetime", models.DateTimeField(null=True)),
                ("time", models.TimeField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(null=True)),
                ("deleted_at", models.DateTimeField(null=True)),
                ("created_by", models.BigIntegerField(null=True)),
                ("updated_by", models.BigIntegerField(null=True)),
                ("deleted_by", models.BigIntegerField(null=True)),
            ],
        ),
    ]