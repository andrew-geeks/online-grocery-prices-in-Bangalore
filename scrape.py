import csv
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import json
import time 

chromedriver_autoinstaller.install()
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(options=chrome_options,executable_path='chromedriver.exe')
f = open('list.json')
j_data = json.load(f)


def getData(fname,url):
    print(fname)
    driver.get(url)
    time.sleep(1)
    value=driver.find_element(By.CLASS_NAME, 'fLZywG')
    value=value.text
    actualPrice=value.split(' ')
    actualPrice = actualPrice[1][1:]
    #print("actualPrice: "+actualPrice)
    
    value1=driver.find_element(By.XPATH, '//*[@id="siteLayout"]/div/div[1]/section[1]/div[2]/section[1]/table/tr[1]/td[2]')
    value1=value1.text
    MRP=value1[1:]
    #print("MRP:"+MRP)
    
    value2 = driver.find_element(By.XPATH,'//*[@id="siteLayout"]/div/div[1]/section[1]/div[2]/section[1]/table/tr[3]/td[2]').text
    amt_discounted_prcntge=value2.split(" ")[0]
    #print("Discount:"+amt_discounted_prcntge)
    
    
    dateval=str(datetime.date.today()) 
    date=dateval.split('-')
    date=date[2]+'-'+date[1]+'-'+date[0] #date
    now = datetime.datetime.now()
    month = now.strftime("%B") #month
    
    #csv
    data=[[date,month,MRP,actualPrice,amt_discounted_prcntge]]
    print(data)
    with open('datasets/'+fname+'price_dataset.csv','a',newline='') as file:
                writer=csv.writer(file)
                writer.writerows(data)




for i in j_data["data"]:
    keys = i.keys()
    values = i.values()
    for j in keys:
        try:
            getData(j,i[j])
        except:
            pass
        
       
driver.close()      
