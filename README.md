# flask_structure-
This application follows a factory pattern and uses Flask Blueprint to create a modular and scalable Flask application. Below is the folder structure of this test application:
                                                                  
                                                                  flask_structure-/
                                                                  ├── app.py├── docker.py
                                                                  ├── flask_simple
                                                                  │   ├── commonutil
                                                                  │   │   ├── commonutil_service.py
                                                                  │   │   └── __init__.py
                                                                  │   ├── config
                                                                  │   │   └── config.py
                                                                  │   ├── db_service
                                                                  │   │   ├── db_common_service.py
                                                                  │   │   ├── db.py
                                                                  │   │   ├── __init__.py
                                                                  │   │   └── models.py
                                                                  │   ├── __init__.py
                                                                  │   ├── routes
                                                                  │   │   ├── __init__.py
                                                                  │   │   └── test_route.py
                                                                  │   ├── schemas
                                                                  │   │   ├── __init__.py
                                                                  │   │   └── test_schema.py
                                                                  │   └── service
                                                                  │       ├── __init__.py
                                                                  │       └── test_service.py
                                                                  ├── migrations
                                                                  │   ├── alembic.ini
                                                                  │   ├── env.py
                                                                  │   ├── README
                                                                  │   ├── script.py.mako
                                                                  │   └── versions
                                                                  │       ├── 697d9a080ff8_initial_migration.py
                                                                  │       └── __pycache__
                                                                  │           └── 697d9a080ff8_initial_migration.cpython-310.pyc
                                                                  ├── README.md
                                                                  ├── requirements.txt
                                                                  ├── tests
                                                                  └── venv


We implemented here as:



-> A simple user registration API is created in test_route.py.

-> It accepts name and email as input.

-> Input validation is performed using Pydantic in test_schema.py.

-> If validation passes, the service processes the data and returns a standardized response.

-> The response format follows a common response structure to ensure consistency.
