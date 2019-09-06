from datetime import datetime

from selenium import webdriver
from selenium_tutorial.diy01.config import NAVER_WEBTOON_URL, favorites
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


__all__ = ['driver']

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get(NAVER_WEBTOON_URL)
name = favorites[datetime.now().weekday()] # '마음의소리'

driver.find_element(By.XPATH, f"//*[text()='{name}']")


driver.find_element(By.XPATH, f"//*[text()='{name}']").click()

latest_episode = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                '#content > table > tbody > tr > td.title'))
)
latest_episode.find_element_by_tag_name('a').click()





