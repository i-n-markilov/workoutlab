from django.db import migrations
from django.utils.text import slugify

EXERCISES = [

    ('Barbell Bench Press',
     'Compound chest exercise using a barbell.',
     '1. Lie flat on a bench with feet firmly on the ground.\n'
     '2. Grip the bar slightly wider than shoulder width.\n'
     '3. Lower the bar slowly to your chest.\n'
     '4. Press the bar upward until arms are fully extended.\n'
     '5. Keep elbows slightly tucked to protect shoulders.',
     'Medium', 'Chest', None, False, ['Barbell']),

    ('Dumbbell Bench Press',
     'Chest press variation using dumbbells.',
     '1. Lie on a bench holding dumbbells at chest level.\n'
     '2. Press dumbbells upward until arms are straight.\n'
     '3. Lower dumbbells slowly to starting position.\n'
     '4. Keep elbows at about 45 degrees from body.\n'
     '5. Maintain core tight and feet on the ground.',
     'Medium', 'Chest', None, False, ['Dumbbells']),

    ('Chest Press Machine',
     'Machine-based chest press movement.',
     '1. Sit with back firmly against the pad.\n'
     '2. Grip handles and press forward until arms are extended.\n'
     '3. Return slowly to starting position.\n'
     '4. Keep movements controlled and avoid locking elbows.',
     'Easy', 'Chest', None, False, ['Chest Press Machine']),

    ('Cable Chest Fly',
     'Isolation chest movement using cables.',
     '1. Stand between the cables and hold handles at shoulder height.\n'
     '2. Step forward slightly and lean a little for balance.\n'
     '3. Bring handles together in front of chest with slight bend in elbows.\n'
     '4. Slowly return to starting position.\n'
     '5. Keep chest up and core engaged.',
     'Medium', 'Chest', None, False, ['Cable Crossover Machine']),

    ('Push-Up',
     'Bodyweight chest pressing exercise.',
     '1. Place hands under shoulders and extend legs behind you.\n'
     '2. Keep body straight from head to heels.\n'
     '3. Lower chest to the floor without sagging hips.\n'
     '4. Push back up until arms are straight.\n'
     '5. Breathe in while lowering, out while pushing.',
     'Easy', 'Chest', None, True, []),

    ('Pull-Up',
     'Vertical pulling movement using bodyweight or bar.',
     '1. Grip pull-up bar with palms facing away from you.\n'
     '2. Hang fully with arms extended.\n'
     '3. Pull chest toward bar by bending elbows.\n'
     '4. Lower body slowly back to starting position.\n'
     '5. Keep core tight and avoid swinging.',
     'Hard', 'Back', None, False, ['Pull-Up Bar']),

    ('Lat Pulldown',
     'Machine-based vertical pulling exercise.',
     '1. Sit at machine and grip bar wider than shoulders.\n'
     '2. Pull bar down to upper chest.\n'
     '3. Control return to starting position.\n'
     '4. Keep back straight and chest up.\n'
     '5. Avoid using momentum.',
     'Medium', 'Back', None, False, ['Lat Pulldown Machine']),

    ('Barbell Bent-Over Row',
     'Compound rowing exercise with barbell.',
     '1. Hold barbell with overhand grip.\n'
     '2. Hinge at hips keeping back flat.\n'
     '3. Pull bar toward lower ribs.\n'
     '4. Lower slowly to starting position.\n'
     '5. Keep elbows close to body and avoid rounding back.',
     'Medium', 'Back', None, False, ['Barbell']),

    ('Seated Cable Row',
     'Cable-based horizontal pulling exercise.',
     '1. Sit upright with feet on platform.\n'
     '2. Grab handle with both hands.\n'
     '3. Pull handle toward torso while squeezing shoulder blades.\n'
     '4. Slowly return to starting position.\n'
     '5. Keep back straight and core tight.',
     'Medium', 'Back', None, False, ['Cable Crossover Machine']),

    ('Suspension Row',
     'Bodyweight row using suspension trainer.',
     '1. Hold suspension straps and lean back.\n'
     '2. Keep body straight from head to heels.\n'
     '3. Pull chest toward handles.\n'
     '4. Lower slowly back to start.\n'
     '5. Engage core throughout movement.',
     'Medium', 'Back', None, False, ['Suspension Trainer']),

    ('Barbell Back Squat',
     'Compound lower body strength movement.',
     '1. Position barbell on upper back.\n'
     '2. Stand with feet shoulder-width apart.\n'
     '3. Squat down until thighs are parallel to floor.\n'
     '4. Push through heels to return to standing.\n'
     '5. Keep chest up and knees aligned with toes.',
     'Medium', 'Legs', None, False, ['Barbell']),

    ('Leg Press',
     'Machine-based lower body pressing exercise.',
     '1. Sit on leg press machine with feet shoulder-width on platform.\n'
     '2. Lower weight slowly toward chest.\n'
     '3. Push platform back up until legs nearly extended.\n'
     '4. Do not lock knees.\n'
     '5. Keep back pressed against seat.',
     'Easy', 'Legs', None, False, ['Leg Press Machine']),

    ('Leg Curl',
     'Isolation hamstring machine exercise.',
     '1. Lie face down on leg curl machine.\n'
     '2. Place ankles under padded lever.\n'
     '3. Curl weight toward glutes slowly.\n'
     '4. Lower back with control.\n'
     '5. Avoid swinging legs.',
     'Easy', 'Legs', None, False, ['Leg Curl Machine']),

    ('Walking Lunges',
     'Unilateral leg movement with dumbbells.',
     '1. Stand tall holding dumbbells by sides.\n'
     '2. Step forward into a lunge, lowering back knee.\n'
     '3. Push through front heel to stand and step forward with other leg.\n'
     '4. Keep torso upright.\n'
     '5. Repeat alternately.',
     'Medium', 'Legs', None, False, ['Dumbbells']),

    ('Bodyweight Squat',
     'Basic lower body bodyweight movement.',
     '1. Stand shoulder-width apart.\n'
     '2. Sit back and lower down as if sitting on a chair.\n'
     '3. Keep chest up and knees in line with toes.\n'
     '4. Push through heels to stand.\n'
     '5. Engage core throughout movement.',
     'Easy', 'Legs', None, True, []),

    ('Kettlebell Swing',
     'Explosive hip hinge using kettlebell.',
     '1. Stand feet shoulder-width apart with kettlebell on floor.\n'
     '2. Hinge at hips, keeping back flat, and grab kettlebell.\n'
     '3. Swing kettlebell back between legs.\n'
     '4. Drive hips forward explosively to swing kettlebell to chest height.\n'
     '5. Control the descent and repeat.',
     'Hard', 'Legs', 'Core', False, ['Kettlebell']),

    ('Barbell Overhead Press',
     'Compound shoulder press with barbell.',
     '1. Stand with feet shoulder-width apart.\n'
     '2. Grip barbell at shoulder height.\n'
     '3. Press bar overhead until arms are straight.\n'
     '4. Lower slowly to shoulders.\n'
     '5. Keep core tight and back neutral.',
     'Medium', 'Shoulders', None, False, ['Barbell']),

    ('Dumbbell Lateral Raise',
     'Isolation shoulder raise movement.',
     '1. Hold dumbbells at sides.\n'
     '2. Raise arms to shoulder height with slight elbow bend.\n'
     '3. Lower slowly back to sides.\n'
     '4. Avoid swinging.\n'
     '5. Keep core engaged.',
     'Medium', 'Shoulders', None, False, ['Dumbbells']),

    ('Shoulder Press Machine',
     'Machine-based shoulder pressing exercise.',
     '1. Sit with back supported.\n'
     '2. Grip handles at shoulder height.\n'
     '3. Press upward until arms are fully extended.\n'
     '4. Lower slowly to start.\n'
     '5. Avoid locking elbows.',
     'Easy', 'Shoulders', None, False, ['Smith Machine']),

    ('Pike Push-Up',
     'Bodyweight shoulder-focused push-up variation.',
     '1. Form inverted V shape with hips raised.\n'
     '2. Lower head toward floor by bending elbows.\n'
     '3. Press back up to starting position.\n'
     '4. Keep legs and core engaged.\n'
     '5. Breathe steadily.',
     'Medium', 'Shoulders', None, True, []),

    ('Barbell Bicep Curl',
     'Barbell curl targeting biceps.',
     '1. Stand with feet shoulder-width apart.\n'
     '2. Hold barbell with palms facing forward.\n'
     '3. Curl bar toward shoulders, keeping elbows close.\n'
     '4. Lower slowly to starting position.\n'
     '5. Avoid swinging arms.',
     'Medium', 'Arms', None, False, ['Barbell']),

    ('Dumbbell Hammer Curl',
     'Neutral grip curl using dumbbells.',
     '1. Hold dumbbells with palms facing inward.\n'
     '2. Curl dumbbells toward shoulders.\n'
     '3. Lower slowly.\n'
     '4. Keep elbows tucked to sides.\n'
     '5. Engage core for stability.',
     'Medium', 'Arms', None, False, ['Dumbbells']),

    ('Tricep Pushdown',
     'Cable-based tricep extension exercise.',
     '1. Stand at cable machine.\n'
     '2. Grip bar with palms facing down.\n'
     '3. Push bar downward until arms are straight.\n'
     '4. Return slowly to start.\n'
     '5. Keep elbows close to body.',
     'Easy', 'Arms', None, False, ['Cable Crossover Machine']),

    ('Dips',
     'Bodyweight tricep-focused movement.',
     '1. Hold parallel bars and lift body.\n'
     '2. Lower slowly by bending elbows.\n'
     '3. Push upward until arms extend.\n'
     '4. Keep torso upright.\n'
     '5. Avoid swinging.',
     'Hard', 'Arms', None, False, ['Pull-Up Bar']),

    ('Battle Rope Slams',
     'Explosive conditioning exercise.',
     '1. Hold ends of ropes.\n'
     '2. Lift ropes overhead.\n'
     '3. Slam them forcefully toward the ground.\n'
     '4. Repeat rhythmically.\n'
     '5. Keep core tight.',
     'Medium', 'Arms', 'Core', False, ['Battle Ropes']),

    ('Plank',
     'Static core stabilization exercise.',
     '1. Position forearms on floor, elbows under shoulders.\n'
     '2. Extend legs behind keeping body straight.\n'
     '3. Hold position, engaging core.\n'
     '4. Avoid hips sagging or raising too high.\n'
     '5. Breathe steadily.',
     'Easy', 'Core', None, True, []),

    ('Hanging Leg Raises',
     'Core exercise performed hanging from a bar.',
     '1. Hang from bar with arms extended.\n'
     '2. Keep legs straight and raise them to hip height or higher.\n'
     '3. Lower legs slowly.\n'
     '4. Keep core tight.\n'
     '5. Avoid swinging.',
     'Hard', 'Core', None, False, ['Pull-Up Bar']),

    ('Russian Twists',
     'Rotational core exercise using weight.',
     '1. Sit on floor, lean back slightly.\n'
     '2. Hold weight in front of chest.\n'
     '3. Rotate torso to the right, then left.\n'
     '4. Keep feet off floor for more challenge.\n'
     '5. Move slowly and control rotation.',
     'Medium', 'Core', None, False, ['Weight Plates']),

    ('Cable Woodchopper',
     'Rotational cable core movement.',
     '1. Stand sideways to cable machine.\n'
     '2. Grip handle with both hands.\n'
     '3. Pull diagonally across body from high to low.\n'
     '4. Return slowly.\n'
     '5. Engage core and avoid twisting spine excessively.',
     'Medium', 'Core', None, False, ['Cable Crossover Machine']),

    ('Mountain Climbers',
     'Dynamic bodyweight core exercise.',
     '1. Start in plank position with arms extended.\n'
     '2. Alternate driving knees toward chest quickly.\n'
     '3. Keep core tight.\n'
     '4. Maintain straight back.\n'
     '5. Breathe steadily and avoid sagging hips.',
     'Easy', 'Core', None, True, []),
]

def add_initial_exercises(apps, schema_editor):
    Exercise = apps.get_model('exercise', 'Exercise')
    Equipment = apps.get_model('equipment', 'Equipment')

    for name, desc, instructions, difficulty, primary, secondary, is_bodyweight, equipment_names in EXERCISES:
        slug = slugify(name)
        exercise, created = Exercise.objects.get_or_create(
            name=name,
            defaults={
                'description': desc,
                'instructions': instructions,
                'difficulty': difficulty,
                'primary_muscle_group': primary,
                'secondary_muscle_group': secondary,
                'is_bodyweight': is_bodyweight,
                'slug': slug,
            },
        )

        if created and equipment_names:
            equipment_objects = Equipment.objects.filter(name__in=equipment_names)
            exercise.equipment.set(equipment_objects)

def remove_initial_exercises(apps, schema_editor):
    Exercise = apps.get_model('exercise', 'Exercise')
    names = [item[0] for item in EXERCISES]
    Exercise.objects.filter(name__in=names).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_alter_exercise_secondary_muscle_group'),
    ]

    operations = [
        migrations.RunPython(add_initial_exercises, remove_initial_exercises),
    ]
