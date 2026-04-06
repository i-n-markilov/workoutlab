#!/bin/bash
cd /home/site/wwwroot
celery -A workoutlab worker --loglevel=info --pool=solo --concurrency=2