from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage():

    input_subscription_xpath = "//input[@id='susbscribe_email']"
    btn_subscription_CSS = "#subscribe"
    txt_subscriptionStatus_xpath = "//div[normalize-space()='You have been successfully subscribed!']"

    def __init__(self, driver):
        self.driver = driver

    def setSubscription(self, email):
        inbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.input_subscription_xpath)))
        inbox.send_keys(email)

    def clickSubscription(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.btn_subscription_CSS)))
        button.click()

    def getSubscriptionStatus(self):
        try:
            status = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.txt_subscriptionStatus_xpath))).text
            print(status)
            return status
        except:
            print("Unable to Find the status message")
