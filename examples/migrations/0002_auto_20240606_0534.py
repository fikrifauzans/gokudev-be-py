from django.db import migrations
import random
import datetime

def add_dummy_data(apps, schema_editor):
    ExampleModel = apps.get_model("examples", "ExampleModel")
    
    for _ in range(1000):
        try:
            ExampleModel.objects.create(
                string=f"Sample String {_}",
                text=f"Sample Text {_}",
                smallint=random.randint(1, 100),
                integer=random.randint(101, 200),
                biginteger=random.randint(201, 300),
                boolean=random.choice([True, False]),
                date=datetime.date(2024, random.randint(1, 12), random.randint(1, 28)),
                datetime=datetime.datetime(
                    2024,
                    random.randint(1, 12),
                    random.randint(1, 28),
                    random.randint(0, 23),
                    random.randint(0, 59),
                ),
                time=datetime.time(
                    random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)
                ),
                created_by=random.randint(1, 10),
                updated_by=random.randint(1, 10),
                deleted_by=random.randint(1, 10),
            )
        except Exception as e:
            print(f"Error creating ExampleModel instance {_}: {e}")

class Migration(migrations.Migration):

    dependencies = [
        ("examples", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_dummy_data),
    ]
