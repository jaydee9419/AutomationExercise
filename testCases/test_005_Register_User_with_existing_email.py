from pageObjects.BasePage import BasePage
from pageObjects.Signup_and_LoginPage import Login
from utilities.readProperties import ReadConfig

class Test_Register_user():
    baseURL = ReadConfig.getApplicationURL()

    def test_registor_user(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.checkWebsiteVisability()
        self.bp.clickLoginSignup()

        self.lsp = Login(self.driver)
        self.lsp.setName(ReadConfig.setUsername())
        self.lsp.setMail(ReadConfig.setMail())
        self.lsp.clickSignup()
        self.lsp.getSignupFailedMsg()


