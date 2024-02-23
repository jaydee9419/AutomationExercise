from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.Signup_and_LoginPage import Login
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
        self.hp.getUsername()
        time.sleep(2)

        self.hp.clickDeleteAccount()
        time.sleep(2)

        del_msg = self.lp.getDeleteconfMsg()
        if del_msg == "ACCOUNT DELETED!":
            assert True
        else:
            assert False
        time.sleep(2)



