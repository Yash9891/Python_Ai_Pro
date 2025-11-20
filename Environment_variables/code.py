import os
from dotenv import load_dotenv

#load env file
load_dotenv()

#pip install python-dotenv
# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL')

print(f"Using database: {database}")
print(f"Using api key: {api_key}")
