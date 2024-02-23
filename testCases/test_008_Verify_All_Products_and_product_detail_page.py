from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.ProductDetailsPage import ProductDetails
import time

class Test_Verify_All_Productsdetail():
    baseURL = ReadConfig.getApplicationURL()

    def test_verify_all_productdetails(self, setup1):
        self.driver = setup1
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.checkWebsiteVisability()
        self.bp.clickProducts()

        self.vapd = ProductDetails(self.driver)
        self.vapd.getPageInfo()
        self.vapd.clickViewProduct()
        self.vapd.getProductInfo()
        self.vapd.getCategoryInfo()
        self.vapd.getPriceInfo()
        self.vapd.getAvailabilityInfo()
        self.vapd.getConditionInfo()
        self.vapd.getBrandInfo()
        time.sleep(3)
        self.driver.quit()


