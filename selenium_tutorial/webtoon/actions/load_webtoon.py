from selenium.webdriver.common.by import By

from selenium_tutorial.webtoon.config import NAVER_WEBTOON_URL


def load_webtoon(driver, name):
    '''
    혹시 실패했다면? fail over
    '''
    driver.get(NAVER_WEBTOON_URL)

    driver.find_element(By.XPATH, f"//*[text()='{name}']" ).click()
    driver.find_element(By.CSS_SELECTOR, ".viewList > tbody:nth-child(4) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)" ).click()



