from datetime import datetime

from selenium import webdriver
import subprocess

from selenium_tutorial.webtoon.actions.load_webtoon_failover import load_webtoon
from selenium_tutorial.webtoon.config import favorites

subprocess.Popen([r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', ' --remote-debugging-port=9222'
                 , '--profile-directory=Profile 1'])

print('continue')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../chromedriver.exe', chrome_options=options)

driver.get('https://www.naver.com')
load_webtoon(driver, favorites[datetime.now().weekday()])



