import csv
from sqlite3 import Date
from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
#from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

#chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

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



driver.get("https://www.bigbasket.com/pd/10000159/fresho-potato-1-kg/")
value=driver.find_element(By.CLASS_NAME, 'IyLvo')
value=value.text
value1=driver.find_element(By.CLASS_NAME, '_2ifWF')
value1=value1.text
value2=driver.find_element(By.XPATH,'//*[@id="40048457"]/tr[3]/td[2]')
amt_discounted_prcntge=value2.text
MRP=value1.split(' ')
MRP=MRP[1] #mrp

actualPrice=value.split(' ')
actualPrice=actualPrice[1] #price
dateval=str(datetime.date.today()) 
date=dateval.split('-')
date=date[2]+'-'+date[1]+'-'+date[0] #date
now = datetime.datetime.now()
month = now.strftime("%B") #month

#csv
data=[[date,month,MRP,actualPrice,amt_discounted_prcntge]]
with open('datasets/potato1kgprice_dataset.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(data)

###########################################################################

driver.get("https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/")
value=driver.find_element(By.CLASS_NAME, 'IyLvo')
value=value.text
value1=driver.find_element(By.CLASS_NAME, '_2ifWF')
value1=value1.text
value2=driver.find_element(By.XPATH,'//*[@id="10000148"]/tr[3]/td[2]')
amt_discounted_prcntge=value2.text
MRP=value1.split(' ')
MRP=MRP[1] #mrp

actualPrice=value.split(' ')
actualPrice=actualPrice[1] #price
dateval=str(datetime.date.today()) 
date=dateval.split('-')
date=date[2]+'-'+date[1]+'-'+date[0] #date
now = datetime.datetime.now()
month = now.strftime("%B") #month

#csv
data=[[date,month,MRP,actualPrice,amt_discounted_prcntge]]
with open('datasets/onion1kgprice_dataset.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(data)

#########################################################################


driver.close()
