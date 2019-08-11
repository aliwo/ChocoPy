from datetime import datetime

from selenium_tutorial.webtoon.driver import driver
from selenium_tutorial.webtoon.config import favorites, account
from selenium_tutorial.webtoon.load_webtoon import load_webtoon
from selenium_tutorial.webtoon.login import login
from selenium_tutorial.webtoon_failover.load_webtoon_failover import load_webtoon as load_webtoon2




# load_webtoon(driver, favorites[datetime.now().weekday()])
login(driver, account)
load_webtoon2(driver, favorites[datetime.now().weekday()])





