####serilazerss#######################
import os

# ... other settings

INSTALLED_APPS = [
    # ... other apps
    'inventory',
    'rest_framework',
    'rest_framework.authtoken',  # Add for token authentication
    'drf_yasg',  # Optional for API documentation
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Add settings for API documentation (optional)
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# ... other settings
##############################################################################################
