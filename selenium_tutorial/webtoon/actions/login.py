from selenium_tutorial.webtoon.config import NAVER_HOME_URL


def login(driver, account):
    '''
    :param driver: chromedriver 객체.
    :param account: {'account': '계정 아이디', 'password': '계정 비밀번호'}
    :return:
    '''
    driver.get(NAVER_HOME_URL)

