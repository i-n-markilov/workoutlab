from django.db import migrations


def add_initial_messages(apps, schema_editor):
    MotivationMessage = apps.get_model("common", "MotivationMessage")

    messages = [
        "Consistency builds champions.",
        "Every rep counts.",
        "Stronger than yesterday.",
        "Discipline over motivation.",
        "Progress, not perfection.",
    ]

    for message in messages:
        MotivationMessage.objects.create(text=message, active=True)


def remove_initial_messages(apps, schema_editor):
    MotivationMessage = apps.get_model("common", "MotivationMessage")

    MotivationMessage.objects.filter(
        text__in=[
            "Consistency builds champions.",
            "Every rep counts.",
            "Stronger than yesterday.",
            "Discipline over motivation.",
            "Progress, not perfection.",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_initial_messages, remove_initial_messages),
    ]