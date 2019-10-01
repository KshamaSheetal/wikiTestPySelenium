import pytest
import requests
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

def test_search(browser):

    baseurl = "https://en.wikipedia.org/wiki/Selenium"

# Open the page https://en.wikipedia.org/wiki/...
    driver = browser
    driver.get(baseurl)
    driver.maximize_window()

# Verify that the external links in “External links“ section work
    ext_links = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div/ul[2]/li/a')
    for link in ext_links:
        r = requests.get(link.get_attribute('href'))
        print(link.get_attribute('href'), r.status_code)
        assert r.status_code == 200


# Click on the “Oxygen” link on the Periodic table at the bottom of the page
    oxy_link = driver.find_element_by_xpath("//a[@title='Oxygen']").click()

# Verify that it is a “featured article”
    featured_check = driver.find_elements_by_xpath("//div[@id='mw-indicator-featured-star']//a//img")
    if len(featured_check) > 0:
        print('This is featured article')
    else:
        print('This is not featured article')

    assert len(featured_check) > 0


#  Take a screenshot of the right hand box that contains element properties
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'), S('Height')) # May need manual adjustment
    now = datetime.datetime.now()
    oEle = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[1]")
    oEle.screenshot("side_panel_screenshot.png")

# Count the number of pdf links in “References“
    ref_sec = driver.find_elements_by_xpath("//div[47]//a[contains(@href,'.pdf')]")

    print("The number of pdf in reference section is " + str(len(ref_sec)))

    # In the search bar on top right enter “pluto” and verify that the 2 nd suggestion
    searchBox = driver.find_element_by_id('searchInput')
    searchBox.send_keys('pluto')
    time.sleep(5)
    second_title = driver.find_element_by_css_selector(".suggestions-results>a:nth-child(2)")
    print("The title of second search result is : ", second_title)
    assert second_title.get_attribute("title") == "Plutonium"




