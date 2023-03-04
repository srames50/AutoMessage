#import necessary selenium drivers and stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from selenium.webdriver.chrome.options import Options
import os

#open a chrome tab with saved login info
PATH = "/Users/"  # enter path here
os.system("open /Users/") # enter path here
time.sleep(4)



#attach functions to existing chrome tab that has been opened
opt=Options()
opt.add_argument('--disable-gpu')
opt.add_experimental_option("debuggerAddress", "localhost:9222")
driver=webdriver.Chrome(executable_path=PATH, options=opt)

# open google chat (direct link to at home modz chat)
driver.get("https://mail.google.com/chat") # enter google chat link here
time.sleep(4)


#type "@home attendance done for" + "current hour"
now = datetime.datetime.now()
currentHour = now.hour
currentHour = currentHour-12
actions = ActionChains(driver)
actions.send_keys('@home attendance done for', ' ', currentHour, 'pm')

#hit send
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(2)

#exit program
driver.quit()
os.system("killall -9 'Terminal'")


# #wait then click on at home modz chat
# time.sleep(5)
# link = driver.find_element(By.XPATH,'//*[@id="space/AAAAXoXg9IE/SCcFR"]/div/div/div[1]/div/div[2]/div[1]')
# link.click()

# #find search bar and click on that
# searchBox = driver.find_element(By.XPATH, '/html/body/c-wiz[1]/div/div/div/div[1]/span/div[2]/div[2]/div/div[3]/div/div/div/c-wiz/div[6]/div[5]/div/c-wiz/div[2]/div[2]/div[1]/div/div[1]/div/div[2]')
# searchBox.click()
