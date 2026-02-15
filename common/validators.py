from django.core.exceptions import ValidationError
import re

def validate_alphanumeric_spaces(value):
    if not re.match(r'^[a-zA-Z0-9\s\-]+$', value):
        raise ValidationError(
            "Only letters, numbers, spaces and hyphens are allowed."
        )
