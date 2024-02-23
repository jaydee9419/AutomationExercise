from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.Signup_and_LoginPage import Login
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

        login_failed_msg = self.lp.getLoginFailedMsg()
        if login_failed_msg == "Your email or password is incorrect!":
            assert True
        else:
            assert False


