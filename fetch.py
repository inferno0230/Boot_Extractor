import os
import requests
import sys

url = "https://gauss-componentotacostmanual-eu.allawnofs.com/component-ota/" # YY/MM/DD/*.zip

def download(url, filename, month):
    dates = ["01" , "02" , "03" , "04" , "05" , "06" , "07" , "08" , "09" ,
           "10" , "11" , "12" , "13" , "14" , "15" , "16" , "17" , "18" ,
           "19" , "20" , "21" , "22" , "23" , "24" , "25" , "26" , "27" ,
           "28" , "29" , "30" , "31"]
    
    
    for date in dates:
        current_url = url+"23/"+month+"/"+date+"/"+filename
        #print(current_url)
        ## curl current url and check if it gets zip file
        r = requests.request("HEAD", current_url)
        #print(date, r.status_code)
        if r.status_code != 404:
            ## if yes, download it
            print("Found file on", current_url)
            break
        else:
            continue        
        
if __name__ == "__main__":
    args = sys.argv[1:]
    download(url, args[0], args[1])