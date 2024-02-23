from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetails():

    txt_allproducts_xpath = "//h2[normalize-space()='All Products']"
    btn_viewproduct_CSS = "a[href='/product_details/1']"
    txt_product_CSS = "div[class='product-information'] h2"
    txt_category_CSS = ("body > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > "
                        "div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p:nth-child(3)")
    txt_price_CSS = "div[class='product-information'] span span"
    txt_availability_xpath = "//div[@class='product-details']//p[2]"
    txt_condition_xpath = "//div[@class='product-details']//p[3]"
    txt_brand_xpath = "//div[@class='product-details']//p[4]"

    input_search_xpath = "//input[@id='search_product']"
    btn_search_xpath = "//button[@id='submit_search']"
    txt_productdetails_xpath = "//div[@class='productinfo text-center']//p[contains(text(),'Blue Top')]"

    input_count_xpath = "//input[@id='quantity']"
    btn_addtocart_xpath = "button[type='button']"

    def __init__(self, driver):
        self.driver = driver

    def getPageInfo(self):
        try:
            products_page = self.driver.find_element(By.XPATH, self.txt_allproducts_xpath).text
            print("Page Headding:", products_page)
            print("Here is the complete product information")
            print("----------------------------------------------")
            return products_page
        except:
            print("Unable to find the All products page")

    def clickViewProduct(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_viewproduct_CSS).click()

    def getProductInfo(self):
        try:
            product_info = self.driver.find_element(By.CSS_SELECTOR, self.txt_product_CSS).text
            print("Product:", product_info)
            return product_info
        except:
            print("Unable to find the product name")

    def getCategoryInfo(self):
        try:
            category_info = self.driver.find_element(By.CSS_SELECTOR, self.txt_category_CSS).text
            print(category_info)
            return category_info
        except:
            print("Unable to find the category of the product")

    def getPriceInfo(self):
        try:
            price_info = self.driver.find_element(By.CSS_SELECTOR, self.txt_price_CSS).text
            print("Price:", price_info)
            return price_info
        except:
            print("Unable to find the price of the product")

    def getAvailabilityInfo(self):
        try:
            available_info = self.driver.find_element(By.XPATH, self.txt_availability_xpath).text
            print(available_info)
            return available_info
        except:
            print("Unable to find the Available status of the product")

    def getConditionInfo(self):
        try:
            condition_info = self.driver.find_element(By.XPATH, self.txt_condition_xpath).text
            print(condition_info)
            return condition_info
        except:
            print("Unable to find the Condition of the product")

    def getBrandInfo(self):
        try:
            brand_info = self.driver.find_element(By.XPATH, self.txt_brand_xpath).text
            print(brand_info)
            return brand_info
        except:
            print("Unable to find the brand of the product")


    def setSearchbox(self):

        search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.input_search_xpath)))
        search_box.send_keys("blue top")


    def clickSearchButton(self):

        search_buttoon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.btn_search_xpath)))
        search_buttoon.click()

    def getSearchedProductInfo(self):
        try:
            product_info = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txt_productdetails_xpath))).text
            print(product_info)
            return product_info
        except:
            print("Unable to find the searched product")

    def setProductCount(self):
        count_box = self.driver.find_element(By.XPATH, self.input_count_xpath)
        count_box.clear()
        count_box.send_keys("5")

    def clickAddtoCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_addtocart_xpath).click()


