from django import template

register = template.Library()

@register.inclusion_tag('equipment/../../templates/exercise/difficulty-bar.html')
def difficulty_bar(value):

    difficulty_visuals = {
        'Easy': (1,'bg-green-500'),
        'Medium': (2,'bg-yellow-500'),
        'Hard': (3,'bg-red-500'),
    }

    filled_in, color = difficulty_visuals.get(value, (0,'bg-gray-300'))

    return {'filled_in': filled_in, 'color': color}