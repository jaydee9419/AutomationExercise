from pageObjects.BasePage import BasePage
from pageObjects.CartPage import CartPage
from utilities.readProperties import ReadConfig
from pageObjects.ProductDetailsPage import ProductDetails
import time



class Test_AddPoducts():
    baseURL = ReadConfig.getApplicationURL()

    def test_addproducts(self, setup1):
        self.driver = setup1
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickProducts()

        self.pdc = ProductDetails(self.driver)
        self.pdc.clickViewProduct()
        self.pdc.setProductCount()
        self.pdc.clickAddtoCart()
        time.sleep(15)

        self.bp.clickCart()
        time.sleep(5)




