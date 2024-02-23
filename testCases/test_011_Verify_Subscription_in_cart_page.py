from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.CartPage import CartPage
import time

class Test_SubscriptionInCart():
    baseURL = ReadConfig.getApplicationURL()

    def test_subscriptionInCart(self, setup1):
        self.driver = setup1
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.checkWebsiteVisability()
        self.bp.clickCart()

        self.cp = CartPage(self.driver)
        self.cp.setSubscription(ReadConfig.setMail())
        time.sleep(2)
        self.cp.clickSubscription()
        time.sleep(3)
        self.cp.getSubscriptionStatus()
        # if message == "You have been successfully subscribed!":
        #     assert True
        # else:
        #     assert False
        time.sleep(2)

