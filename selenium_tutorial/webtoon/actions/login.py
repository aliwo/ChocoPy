from selenium_tutorial.webtoon.config import NAVER_LOGIN_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 이제 캡챠 메세지 뜨는데?

def login(driver, account):
    '''
    :param driver: chromedriver 객체.
    :param account: {'account': '계정 아이디', 'password': '계정 비밀번호'}
    :return:
    '''
    driver.get(NAVER_LOGIN_URL)

    id_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'id'))
    )
    id_field.send_keys(account['account'])

    pw_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'pw'))
    )
    pw_field.send_keys(account['password'])

    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#frmNIDLogin > fieldset > input'))
    )

    login_button.click()



