from selenium_tutorial.webtoon.driver.driver import driver
from selenium.webdriver.common.by import By

driver.get('https://cookie.riimu.net/speed/')

img = driver.find_element(By.ID, 'virtualCookie')
for _ in range(1000):
    img.click()

