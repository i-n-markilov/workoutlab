from django.db import migrations
from django.utils.text import slugify

EQUIPMENT_ITEMS = [
    ('Adjustable Bench', 'Free weights', 'Versatile bench used for various strength training exercises.'),
    ('Assault Bike', 'Cardio', 'High-intensity air resistance stationary bike for cardio workouts.'),
    ('Barbell', 'Free weights', 'Long weighted bar used for compound strength exercises.'),
    ('Battle Ropes', 'Functional tool', 'Heavy ropes used for full-body conditioning and endurance training.'),
    ('Cable Crossover Machine', 'Resistance machine', 'Machine with adjustable pulleys for isolated muscle exercises.'),
    ('Chest Press Machine', 'Resistance machine', 'Machine designed to target chest muscles safely.'),
    ('Dumbbells', 'Free weights', 'Handheld weights used for strength and resistance training.'),
    ('Elliptical Trainer', 'Cardio', 'Low-impact cardio machine simulating walking or running.'),
    ('Exercise Bike', 'Cardio', 'Stationary bike used for cardiovascular training.'),
    ('Kettlebell', 'Free weights', 'Cast-iron weight used for dynamic strength and conditioning exercises.'),
    ('Lat Pulldown Machine', 'Resistance machine', 'Machine targeting the back and lat muscles.'),
    ('Leg Curl Machine', 'Resistance machine', 'Machine designed to isolate the hamstring muscles.'),
    ('Leg Press Machine', 'Resistance machine', 'Machine used to strengthen quadriceps, hamstrings, and glutes.'),
    ('Pull-Up Bar', 'Functional tool', 'Bar used for upper body pulling exercises.'),
    ('Resistance bands', 'Functional tool', 'Elastic bands offering variable resistance for strength training, warm-ups, and rehabilitation exercises.'),
    ('Rowing Machine', 'Cardio', 'Cardio machine simulating rowing for full-body conditioning.'),
    ('Smith Machine', 'Resistance machine', 'Guided barbell machine for controlled strength training.'),
    ('Stair Climber', 'Cardio', 'Machine simulating stair climbing for lower body cardio workouts.'),
    ('Suspension Trainer', 'Functional tool', 'Bodyweight training system using adjustable straps.'),
    ('Treadmill', 'Cardio', 'Machine for walking, jogging, or running indoors.'),
    ('Weight Plates', 'Free weights', 'Weighted plates used with barbells and machines.'),
]


def add_initial_equipment(apps, schema_editor):
    Equipment = apps.get_model('equipment', 'Equipment')

    for name, type_value, description in EQUIPMENT_ITEMS:
        slug=slugify(name)
        Equipment.objects.get_or_create(
            name=name,
            defaults={
                'type': type_value,
                'description': description,
                'slug': slug,
            },
        )


def remove_initial_equipment(apps, schema_editor):
    Equipment = apps.get_model('equipment', 'Equipment')

    names = [item[0] for item in EQUIPMENT_ITEMS]
    Equipment.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_equipment, remove_initial_equipment),
    ]
