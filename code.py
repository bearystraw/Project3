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

pattern = r'\(\d{2}/\w{3}/\d{4})'
dates = [re.search(pattern, line).group(1) for line in log_content if re.search(pattern, line)]

date_objectives = [datetime.strptime(date, "%d/%b%Y") for date in dates]
return date_objects

def get_request_counts(dates):
   end_date = dates[-1]
   six_months_ago = end_date - timedelta(days=6*30)

   last_six_months_count = sum(1 for date in dates if date > six_months_ago)
   total_requests = len(dates)

   return total_requests, last_six_months_count

def display_results(total, last_six_months):
   print(f"Total requests in the last 6 months: {last_six_months}")
   print(f"Total requests in the log: {total}")

def main():
   download_log()
   dates = parse_dates_from_log()
   total, last_six_months = get_request_counts(dates)
   display_results(total, last_six_months)

if __name__ == "__main__":
   main()
