from selenium.webdriver.common.by import By


class RegiserPage():
    txt_enteraccount_xpath = "//b[normalize-space()='Enter Account Information']"
    rdb_gender_xpath = "//input[@id='id_gender1']"

    input_password_xpath = "//input[@id='password']"

    input_days_xpath = "//select[@id='days']"
    input_months_xpath = "//select[@id='months']"
    input_years_xpath = "//select[@id='years']"

    box_newslatter_xpath = "//input[@id='newsletter']"
    box_offers_xpath = "//input[@id='optin']"

    input_fname_xpath = "//input[@id='first_name']"
    input_lname_xpath = "//input[@id='last_name']"
    input_company_xpath = "//input[@id='company']"

    input_address1_xpath = "//input[@id='address1']"
    input_address2_xpath = "//input[@id='address2']"

    input_state_xpath = "//input[@id='state']"
    input_city_xpath = "//input[@id='city']"
    input_zipcode_xpath = "//input[@id='zipcode']"
    input_phone_xpath = "//input[@id='mobile_number']"
    btn_create_xpath = "//button[normalize-space()='Create Account']"

    btn_continue_xpath = "//a[normalize-space()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def getRegPageVisable(self):
        try:
            regPage = self.driver.find_element(By.XPATH, self.txt_enteraccount_xpath).text
            return regPage

        except:
            print("New user Registration page not visible")

    def setGender(self):
        self.driver.find_element(By.XPATH, self.rdb_gender_xpath).click()

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(pwd)

    def setDay(self, day):
        self.driver.find_element(By.XPATH, self.input_days_xpath).send_keys(day)

    def setMonth(self, month):
        self.driver.find_element(By.XPATH, self.input_months_xpath).send_keys(month)

    def setYear(self, year):
        self.driver.find_element(By.XPATH, self.input_years_xpath).send_keys(year)

    def clickNewslatter(self):
        self.driver.find_element(By.XPATH, self.box_newslatter_xpath).click()

    def clickOffers(self):
        self.driver.find_element(By.XPATH, self.box_offers_xpath).click()

    def setFirstname(self, fname):
        self.driver.find_element(By.XPATH, self.input_fname_xpath).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(By.XPATH, self.input_lname_xpath).send_keys(lname)

    def setCompany(self, company):
        self.driver.find_element(By.XPATH, self.input_company_xpath).send_keys(company)

    def setAddress1(self, add1):
        self.driver.find_element(By.XPATH, self.input_address1_xpath).send_keys(add1)

    def setAddress2(self, add2):
        self.driver.find_element(By.XPATH, self.input_address2_xpath).send_keys(add2)


    def setState(self, state):
        self.driver.find_element(By.XPATH, self.input_state_xpath).send_keys(state)

    def setCity(self, city):
        self.driver.find_element(By.XPATH, self.input_city_xpath).send_keys(city)

    def setZipcode(self, zipcode):
        self.driver.find_element(By.XPATH, self.input_zipcode_xpath).send_keys(zipcode)

    def setPhone(self, phone):
        self.driver.find_element(By.XPATH, self.input_phone_xpath).send_keys(phone)

    def clickCreate(self):
        self.driver.find_element(By.XPATH, self.btn_create_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
