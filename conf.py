import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ.get('OPENAI_API_KEY')
