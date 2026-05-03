import os
from dotenv import load_dotenv
load_dotenv()
FOUNDRY_PROJECT_ENDPOINT = os.getenv('FOUNDRY_PROJECT_ENDPOINT')
FOUNDRY_AGENT_ID = os.getenv('FOUNDRY_AGENT_ID')
