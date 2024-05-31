# serverless_function.py

import os
from django.core.asgi import get_asgi_application

# Set the Django settings module for the serverless function
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

# Initialize the Django application
django_application = get_asgi_application()

# Define the handler function for the serverless function
def handler(request, response):
    # Process the incoming HTTP request using the Django application
    django_response = django_application(request)
    
    # Copy the Django response headers and content to the serverless function response
    response.status_code = django_response.status_code
    for header, value in django_response.items():
        response.set_header(header, value)
    
    # Return the Django response content
    return django_response.content
