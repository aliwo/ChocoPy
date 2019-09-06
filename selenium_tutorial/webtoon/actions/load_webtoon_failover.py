from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_tutorial.webtoon.config import NAVER_WEBTOON_URL


def load_webtoon(driver, name):
    driver.get(NAVER_WEBTOON_URL)

    driver.find_element(By.XPATH, f"//*[text()='{name}']" ).click()
    latest_episode = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    '#content > table > tbody > tr > td.title'))
    )

    latest_episode.find_element_by_tag_name('a').click()

