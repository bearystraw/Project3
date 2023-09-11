import urllib.request as web
from datetime import datetime

def log_file_reader(http_access_log):
    
    # Get all IP addresses from the log file
    with open(http_access_log) as f:
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regex, log)
        return ip_list
    

log_file = open(filename, "r+")
for row in log_file:
    print(row)
    regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_list = re.findall(regex, row)
    print()
    return ip_list
pass

#trial 3
parsed_data = []
  
with open("http_access_log","r") as file:
    prev_time = ""
    data = {}
    for line in file:
        time = line.split("[")[1].split("]")[0].split(" ")[0]
        status_code = line.split('"')[2].split(" ")[1]
        if prev_time != "":
            if time == prev_time:
                data[time]["count"] = data[time]["count"] + 1
                if status_code in data[time]:
                    data[time][status_code] = data[time][status_code] + 1
                else:
                    data[time][status_code] = 1
            else:
                prev_time = time
                parsed_data.append(data)
                data = {}
                data[time] = {"count": 1, status_code: 1}
        else:
            prev_time = time
            data[time] = {"count": 1, status_code: 1}

for i in parsed_data:
    print(i)
