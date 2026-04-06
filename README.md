# WorkoutLab 🏋️‍♂️

WorkoutLab is a robust, Django-based fitness management platform designed to help users track equipment, browse exercises, and build customized workout routines.

Currently hosted on : Azure
[WorkoutLab](https://workoutlab.azurewebsites.net/)

## Test users created:

### Normal user
- `username`: user-softuni
- `email`: user-softuni@workoutlab.com
- `pass`: 12user34

### Moderator
- `username`: moderator-softuni
- `email`: moderator-softuni@workoutlab.com
- `pass`: 12staff34

## 🌟 Features

- **Workout Plan Builder**: Create structured workout routines with a dynamic inline exercise formset.
- **Exercise Database**: Explore exercises categorized by difficulty level (via custom template tags), primary muscle group, and required equipment.
- **Equipment Management**: Track gym gear and categorize by type.
- **REST API**: Provides endpoints for integrating workout and equipment data with third-party clients, built with Django REST Framework.
- **Asynchronous Tasks**: Background task processing for email notifications and user onboarding, using Celery WebJob
- **Automated Profiles**: User profiles are automatically created and managed via Django signals.
- **Modern UI**: Responsive design built with Tailwind CSS.
- **Cloud Storage**: Media assets managed via Cloudinary.
- **Predefined Data**: Variety of exercises and equipment available out-of-the-box via data migrations.

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Django 6.0.2, Django REST Framework
- **Frontend**: Tailwind CSS (compiled via PostCSS/npm), Django Templates, Custom Template Tags
- **Forms**: Django Crispy Forms (Tailwind pack)
- **Database**: PostgreSQL
- **Media**: Cloudinary
- **Static Assets**: WhiteNoise
- **Tasks**: Django Background Tasks

## 📂 Project Structure

- `accounts/`: User management, profile signals, and custom group template filters.
- `common/`: Core abstract models, shared validators, and **REST API** endpoints.
- `equipment/`: Management of gym tools and equipment types.
- `exercise/`: Detailed exercise definitions, muscle groups, difficulty levels, and custom difficulty-bar template tags.
- `workout/`: Workout plan management featuring inline formsets.
- `static/`: Project assets, including compiled CSS in `dist/`.
- `templates/`: Structured HTML templates using inheritance and partials.

## 🚀 Getting Started (local setup)

### 1. Prerequisites
- Python 3.10+
- Node.js (for frontend asset compilation)
- PostgreSQL

### 2. Installation
```bash
git clone https://github.com/your-username/workoutlab.git
cd workoutlab
```

### 3. Setup Virtual Environment & Dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
npm install
```

### 4. Configure Environment Variables
Copy the `.env.template` file to `.env` and configure:
- `SECRET_KEY`: Django secret key.
- `DATABASE_URL`: PostgreSQL connection string.
- `CLOUDINARY_URL`: Cloudinary credentials.
- `EMAIL_HOST` / `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD`: SMTP settings for background emails.
- Rest of environment variables.

### 5. Build Assets & Database
```bash
npm run build:css
python manage.py migrate
```

### 6. Run Application
1. **Server**: `python manage.py runserver`
