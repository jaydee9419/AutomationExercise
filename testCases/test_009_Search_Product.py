from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.ProductDetailsPage import ProductDetails
import time

class Test_SearchProduct():
    baseURL = ReadConfig.getApplicationURL()

    def test_searchproduct(self, setup1):
        self.driver = setup1
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.checkWebsiteVisability()
        self.bp.clickProducts()

        self.vapd = ProductDetails(self.driver)
        self.vapd.getPageInfo()

        self.vapd.setSearchbox()

        self.vapd.clickSearchButton()

        self.vapd.getSearchedProductInfo()
        time.sleep(20)
