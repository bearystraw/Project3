#we worked together on brandon's computer and split up typing the code onto here
import urllib.request
import os
import re
from datatime import datetime, timedelta

FILE_URL = "https://s3.amazonaws.com/tcmg476/http_access_log"
LOCAL_FILE = "http_access_log.txt"

def download_log():
   if not os.path.exists(LOCAL_FILE):
      urllib.request.urlretrieve(FILE_URL, LOCAL_FILE)

def parse_dates_from_log():
   with open(LOCAL_FILE, 'r') as f:
      log_content = f.readlines()

pattern = r'\[(\d{2}/\w{3}/\d{4})'
dates = [re.search(pattern, line).group(1) for line in log)content if re.search(pattern, line)]

date_objectives = [datetime.strptime(date, "%d/%b%Y") for date in dates]
return date_objects
