from apps.app import create_app

application = create_app()

# uvicorn wsgi:application --host 0.0.0.0 --port 9000