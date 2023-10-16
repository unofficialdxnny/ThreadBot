from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import os
import json


config = open('config.json', 'r')
data = json.load(config)


## headless = False
options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument(f"--user-data-dir={data['path_to_user_data']}")
options.add_argument(f'--profile-directory={data["path_to_chrome"]}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options) ## Initialise the driver
driver.get("https://threads.net") ## login to snapchat
## driver.maximize_window()
wait = WebDriverWait(driver, 100)

os.system('cls & title Threads Bot')
banner = '''




'''


print(banner)


thread = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]')
post = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div')


while True:
    sleep(5)
    thread.click()
    thread.send_keys('Automating Threads')
    post.clic()