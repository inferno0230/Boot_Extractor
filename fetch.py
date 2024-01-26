import os
import requests
import sys
import subprocess
import json

url = "https://gauss-componentotacostmanual-eu.allawnofs.com/component-ota/" # YY/MM/DD/*.zip

def download(url, filename, month, otaName):
    dates = ["01" , "02" , "03" , "04" , "05" , "06" , "07" , "08" , "09" ,
           "10" , "11" , "12" , "13" , "14" , "15" , "16" , "17" , "18" ,
           "19" , "20" , "21" , "22" , "23" , "24" , "25" , "26" , "27" ,
           "28" , "29" , "30" , "31"]
    
    for date in dates:
        currect_date = date
        current_url = url+"24/"+month+"/"+date+"/"+filename
        #print(current_url)
        ## curl current url and check if it gets zip file
        r = requests.request("HEAD", current_url)
        #print(date, r.status_code)
        if r.status_code != 404:
            data = {}
            data["Date"] = r.headers.get("Date")
            data["Last Modified"] = r.headers.get("Last-Modified")
            data["Content-Size"] = round((int(r.headers.get("Content-Length"))/1024**3),2)
            data["Content-Type"] = r.headers.get("Content-Type")
            data["server"] = r.headers.get("server")
            data["Link"] = current_url
            # Dump data into metadata.json with data in seperate lines
            with open(otaName+".json", "w") as f:
                json.dump(data, f, indent=4)
            
            user = subprocess.run(["whoami"] , capture_output=True, text=True).stdout.strip()
            if user == "inferno0230":
                print("Downloading file...")
                subprocess.run(["axel -a -n $(nproc --all)", current_url])
                subprocess.run(["ln", "-s", filename, otaName+".zip"])
            break
        else:
            continue        
        
if __name__ == "__main__":
    args = sys.argv[1:]
    download(url, args[0], args[1], args[2])
