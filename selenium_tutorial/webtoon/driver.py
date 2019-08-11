from selenium import webdriver

__all__ = ['driver']


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome('../chromedriver.exe', chrome_options=opts)

