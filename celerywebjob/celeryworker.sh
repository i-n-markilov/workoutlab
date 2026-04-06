#!/bin/bash
# WebJob entry point

# Create/activate virtual environment
python3 -m venv "$HOME/venv"
source "$HOME/venv/bin/activate"

# Install dependencies
pip install --upgrade pip
pip install -r "$(dirname "$0")/requirements.txt"

# Navigate to Django app root
cd /home/site/wwwroot || exit 1

# Make sure Python can import your Django project
export PYTHONPATH=$PWD
export DJANGO_SETTINGS_MODULE=workoutlab.settings

# Start Celery worker
celery -A workoutlab worker --loglevel=info --pool=solo --concurrency=2