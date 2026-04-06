#!/bin/bash

cd /home/site/wwwroot || exit 1

export PATH="$HOME/.local/bin:$PATH"

celery -A workoutlab worker --loglevel=info --pool=solo --concurrency=2