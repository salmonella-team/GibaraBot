# setting.py

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GIBARA_TOKEN = os.environ.get("GIBARA_TOKEN")
MAKE_CHANNEL_CATEGORY_ID = os.environ.get("MAKE_CHANNEL_CATEGORY_ID")