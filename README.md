# WorkoutLab 🏋️‍♂️

WorkoutLab is a basic Django-based fitness management platform designed to help users track equipment, browse exercises, and build customized workout routines.

## 🌟 Features

- **Workout Plan Builder**: Create structured workout routines with a dynamic inline exercise formset.
- **Exercise Database**: Explore exercises categorized by difficulty level, primary muscle group, and required equipment.
- **Equipment Management**: Keep track of gym gear and categorize them by type (Cardio, Free Weights, etc.).
- **User-Friendly UI**: Modern, responsive design built with Tailwind CSS and Django Crispy Forms.
- **Predefined data**: Variety of available equipment and exercises included from the get-go for.

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django 6.0
- **Frontend**: Tailwind CSS (via CDN), Django Templates
- **Forms**: Django Crispy Forms (Tailwind template pack)
- **Database**: PostgreSQL (configured via `psycopg2`)

## 📂 Project Structure

- `common/`: Core abstract models, shared validators, search forms, and the landing page logic.
- `equipment/`: Management of gym tools and equipment types.
- `exercise/`: Detailed exercise definitions, muscle groups, and difficulty levels.
- `workout/`: Workout plan management featuring inline formsets for linking exercises to plans.
- `static/`: Project assets (logos, default icons, and images).
- `templates/`: Structured HTML templates using template inheritance and partials.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- pip (Python package manager)

### 2. Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/your-username/workoutlab.git
cd workoutlab
```

### 3. Setup Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4. Configure Environment Variables
Copy the .env.template file:
```bash
cp .env.template .env
```

Edit the .env file and fill in the required values, such as:
- `SECRET_KEY`: A secret key for Django.
-  `Database connection settings`: DB_NAME, DB_USER, DB_PASSWORD, etc.
-  `DEBUG`: Set to True for development, False for production.


### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Database Setup
Run migrations to set up the database schema:
```bash
python manage.py migrate
```

### 7. Start the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to explore WorkoutLab.

