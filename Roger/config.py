import os

# Database Configuration
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_USER = os.getenv('DATABASE_USER', 'user')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'dbname')

# Environment Variables
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Settings
DEBUG = ENVIRONMENT == 'development'