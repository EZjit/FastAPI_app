from dotenv import load_dotenv
import os

load_dotenv()

# PostgreSQL
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASS', 'postgres')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'postgres')


# PostgreSQL test
DB_USER_TEST = os.environ.get('DB_USER_TEST', 'postgres')
DB_PASS_TEST = os.environ.get('DB_PASS_TEST', 'postgres')
DB_HOST_TEST = os.environ.get('DB_HOST_TEST', '127.0.0.1')
DB_PORT_TEST = os.environ.get('DB_PORT_TEST', '5432')
DB_NAME_TEST = os.environ.get('DB_NAME_TEST', 'postgres')

# Secret keys
JWT_SECRET = os.environ.get('JWT_SECRET', 'secret')
AUTH_SECRET = os.environ.get('AUTH_SECRET', 'secret')

# SMTP
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_PORT = os.environ.get('SMTP_PORT')

# Redis
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
