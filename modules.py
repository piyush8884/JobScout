#Use this Url and change city or role accordingly
import pandas as pd
import os
from itertools import chain
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

from random import randint
from selenium.webdriver.support.ui import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class DriverLoadingException(Exception):
    pass
List_of_all = []
options = Options()

options.add_argument("--start-fullscreen")

#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
class DriverLoadingException(Exception):
    pass
List_of_all = []
options = Options()
# options.add_argument("--window-size=1920x1080")
options.add_argument("--start-fullscreen")
# options.add_argument("--verbose")
options.add_argument("--headless")
# options.add_argument("--start-maximized")

# Get the current window size
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# url1=input("Enter the Url :: ")



try:
    with open("url.txt", "r") as file:
        url1 = file.read().strip()
    # Load the URL in the driver
    driver.get(url1)
    #print("driver Opened")
    # Wait for the driver to finish loading
    wait_time = 20
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'nav__button-tertiary') and contains(@class, 'btn-md') and contains(@class, 'btn-tertiary')]"))
    )

    #print("found")

    # Once the driver finishes loading, send a message or perform desired actions

except TimeoutException:
    raise DriverLoadingException("Failed to load the URL within the specified time")









#https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analyst&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'