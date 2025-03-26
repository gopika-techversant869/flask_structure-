
import os
from dotenv import load_dotenv

"""
This file handles environment-specific configurations (local, UAT, production).
It manages sensitive credentials and settings including for example:
- Database connection parameters
- JWT secret keys
- Access and Refresh token configurations
- Environment-specific settings

Usage:
    - Create appropriate .env files (.env.local, .env.uat, .env.production)
    - Set FLASK_ENV environment variable to 'local', 'uat', or 'production'
    - Configuration will be loaded based on the environment

Security Note:
    - Never commit .env files to version control
    - Use strong, unique secrets for each environment
    - Regularly rotate credentials and keys
    - For production, we can implement secrets manager to store credentials securely. ->(Future)
    - Here we can implement a dynamic config system which can be changed based on the environment
      without changing the code. ->(Future)

Additional configurations can be added to each environment class as needed.

we configure the config file at the __init__.py file
"""

ENVIRONMENT = os.getenv('FLASK_ENV', 'local')

if ENVIRONMENT == 'production':
    load_dotenv('.env.production')
elif ENVIRONMENT == 'uat':
    load_dotenv('.env.uat')
else:
    load_dotenv('.env.local')

class BaseConfig:
    """Base configuration class"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def get_database_url():
        return f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

class LocalConfig(BaseConfig):
    """Local environment configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = BaseConfig.get_database_url()
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 900))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 86400))

class UATConfig(BaseConfig):
    """UAT environment configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = BaseConfig.get_database_url()
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 1800)) 
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 86400))

class ProductionConfig(BaseConfig):
    """Production environment configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = BaseConfig.get_database_url()
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600)) 
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 86400))

config = {
    'local': LocalConfig,
    'uat': UATConfig,
    'production': ProductionConfig,
    'default': LocalConfig
}

def get_config():
    return config.get(ENVIRONMENT, config['default'])





