from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


# regular driver
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


# driver with stop ad-based popups
@pytest.fixture()
def setup1():
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.javascript': 2})
    driver = webdriver.Chrome(options=chrome_options)
    return driver


