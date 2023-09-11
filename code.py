#we coded together on brandon's computer and split up the typing of the code
import urllib.request
import os
import re
from datatime import datetime, timedelta

FILE_URL = "https://s3.amazonaws.com/tcmg476/http_access_log"
LOCAL_FILE = "http_access_log.txt"

def download_log():
   if not os.path.exists(LOCAL_FILE):
      urllib.request.urlretrieve(FILE_URL, LOCAL_FILE)
