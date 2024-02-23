from selenium.webdriver.common.by import By



class BasePage():
    txt_home_xpath = "//a[normalize-space()='Home']"
    btn_home_xpath = "//a[normalize-space()='Home']"
    btn_loginsignup_xpath = "//a[normalize-space()='Signup / Login']"
    btn_textcase_xpath = "//a[normalize-space()='Test Cases']"
    btn_products_xpath = "//a[@href='/products']"
    btn_cart_xpath = "//a[normalize-space()='Cart']"

    def __init__(self, driver):
        self.driver = driver

    def checkWebsiteVisability(self):
        print("URL of the current webpage:", self.driver.current_url)
        print("Title of the webpage:", self.driver.title)

    def clickHome(self):
        self.driver.find_element(By.XPATH, self.btn_home_xpath).click()

    def clickLoginSignup(self):
        self.driver.find_element(By.XPATH, self.btn_loginsignup_xpath).click()

    def clickTestcases(self):
        self.driver.find_element(By.XPATH, self.btn_textcase_xpath).click()

    def clickProducts(self):
        self.driver.find_element(By.XPATH, self.btn_products_xpath).click()

    def clickCart(self):
        self.driver.find_element(By.XPATH, self.btn_cart_xpath).click()













