import urllib.request as web
from datetime import datetime

def parse_dates_from_log():
   with open(LOCAL_FILE, 'r') as f:
    log_content = f.readlines()

pattern = r'\[(\d{2}/\w{3}/\d{4})'
dates = [re.search(pattern, line).group(1) for
