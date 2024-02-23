from utilities.readProperties import ReadConfig
from pageObjects.BasePage import BasePage
from pageObjects.Signup_and_LoginPage import Login
from pageObjects.HomePage import HomePage
from pageObjects.RegisterPage import RegiserPage
from utilities import randomStringGenerate
import os


class Test_Registration():
    baseURL = ReadConfig.getApplicationURL()

    def test_registration(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickLoginSignup()

        self.lsp = Login(self.driver)

        self.lsp.setName(ReadConfig.setUsername())
        self.lsp.setMail("dileep@gmail.com")
        self.lsp.clickSignup()

        self.rp = RegiserPage(self.driver)
        conf_msg = self.rp.getRegPageVisable()
        if conf_msg == "ENTER ACCOUNT INFORMATION":
            print(conf_msg)
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "RegPage.png")
            assert False

        self.rp.setGender()
        self.rp.setPassword(ReadConfig.setPassword())

        self.rp.setDay(ReadConfig.setDay())
        self.rp.setMonth(ReadConfig.setMonth())
        self.rp.setYear(ReadConfig.setYear())

        self.rp.clickNewslatter()
        self.rp.clickOffers()

        self.rp.setFirstname(ReadConfig.setFirstname())
        self.rp.setLastname(ReadConfig.setLastname())
        # self.bp.setCompany()

        self.rp.setAddress1(ReadConfig.setAddress())
        self.rp.setAddress2(ReadConfig.setAddress2())

        self.rp.setState(ReadConfig.setState())
        self.rp.setCity(ReadConfig.setCity())
        self.rp.setZipcode(ReadConfig.setZipcode())
        self.rp.setPhone(ReadConfig.setPhone())

        self.rp.clickCreate()
        self.rp.clickContinue()
        self.hp = HomePage(self.driver)
        self.hp.getUsername()

        # self.bp.clickDeleteAccount()
        # self.bp.clickContinue()
        self.driver.close()







