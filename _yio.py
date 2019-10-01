import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import datetime
import time


@pytest.fixture
def browser ():
    options = webdriver.ChromeOptions()
    options.headless = False

    driver = webdriver.Chrome('D:/Python/drivers/chromedriver.exe', options=options)  # Optional argument, if not specified will search path.
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
