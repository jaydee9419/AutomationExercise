from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.Signup_and_LoginPage import Login
from pageObjects.ContactUsPage import ContactUs
from pageObjects.HomePage import HomePage
import time


class Test_Login():
    baseURL = ReadConfig.getApplicationURL()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickLoginSignup()

        self.lp = Login(self.driver)
        self.lp.getConfMsg()
        self.lp.setEmail(ReadConfig.setMail())
        self.lp.setPassword(ReadConfig.setPassword())
        self.lp.clickLogin()

        self.hp = HomePage(self.driver)
        self.hp.clickContactus()

        self.cp = ContactUs(self.driver)
        self.cp.setName(ReadConfig.setUsername())
        self.cp.setMail(ReadConfig.setMail())
        self.cp.setSubject()
        self.cp.setMessage()
        self.cp.uploadFile()
        self.cp.clickSubmit()
        time.sleep(3)
        self.cp.getConfirmationMsg()
        time.sleep(3)
        self.cp.clickHome()
        time.sleep(3)
        self.driver.quit()
