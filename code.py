import urllib.request as web
from datetime import datetime

def parse_dates_from_log():
    dl = web.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    with open('http_access_log', 'wb') as file:
        file.write(dl.read())
    
