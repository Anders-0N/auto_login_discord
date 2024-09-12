import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    '--login',
    dest = 'login',
    required = True,
    help = 'Username Discord',
    metavar = 'user@domen.com',
    type = str
)
parser.add_argument(
    '--password',
    dest = 'password',
    required = True,
    help = 'Password Discord',
    metavar = '********',
    type = str
)
username = parser.parse_args().login
password = parser.parse_args().password

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://discord.com/login")
driver.implicitly_wait(5)
driver.find_element(By.NAME, "email").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)
#driver.quit()
