import csv
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import edgedriver_autoinstaller
from selenium.webdriver.common.by import By
import datetime
import json

edgedriver_autoinstaller.install() 
driver = webdriver.Edge()
driver.get("http://www.python.org")
assert "Python" in driver.title
