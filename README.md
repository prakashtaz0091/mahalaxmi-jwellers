# Django Project

This is a basic Django project that demonstrates how to set up a simple web application using Django.

## Requirements

Before running this project, make sure you have the following installed:

- Python 3.8+
- pip (Python package installer)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

```

git clone https://github.com/prakashtaz0091/mahalaxmi-jwellers
cd <project-directory>

```

2. **Set up a virtual environment (optional but recommended):**

- Create a virtual environment:

  ```
  python -m venv venv
  ```

- Activate the virtual environment:
  - On Windows:
    ```
    venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```
    source venv/bin/activate
    ```

3. **Install the project dependencies:**

- Run the following command to install all required packages from the `requirements.txt` file:
  ```
  pip install -r requirements.txt
  ```

## Database Setup

1. **Apply migrations:**

Django uses migrations to manage the database schema. Run the following command to create the necessary database tables:

```

python manage.py migrate

```

2. **Create a superuser (optional):**

You can create an admin user to log into the Django admin interface:

```

python manage.py createsuperuser

```

Follow the prompts to create a username, email, and password.

## Running the Project

To start the development server, run:

```

python manage.py runserver

```

By default, the server will run on `http://127.0.0.1:8000/`.

## Admin Panel

Once the server is running, you can access the Django admin panel by visiting:

```

http://127.0.0.1:8000/admin/

```

Log in with the superuser credentials you created earlier.

## Notes

- The default port for the development server is 8000. You can change this by specifying a different port when running the `runserver` command (e.g., `python manage.py runserver 8080`).
- This project is set up for local development. For deployment, additional configuration and settings are needed.
