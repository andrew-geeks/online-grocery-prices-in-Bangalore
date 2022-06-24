import csv
from sqlite3 import Date

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import datetime

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

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

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

#driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.bigbasket.com/pd/40048457/fresho-potato-new-crop-1-kg/")
value = driver.find_element_by_class_name('IyLvo')
value=value.text
value1 = driver.find_element_by_class_name('_2ifWF')
value1=value1.text

MRP=value1.split(' ')
MRP=MRP[1] #mrp

actualPrice=value.split(' ')
actualPrice=actualPrice[1] #price
driver.close()

amt_discounted= float(MRP) - int(actualPrice)
amt_discounted_prcntge = (amt_discounted/float(MRP))*100
amt_discounted_prcntge = str(amt_discounted_prcntge)+"%" #discounted_price

dateval=str(datetime.date.today()) 
date=dateval.split('-')
date=date[2]+'-'+date[1]+'-'+date[0] #date
now = datetime.datetime.now()
month = now.strftime("%B") #month

#csv
data=[[date,month,MRP,actualPrice,amt_discounted_prcntge]]
with open('datasets/potatoprice_dataset.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(data)
