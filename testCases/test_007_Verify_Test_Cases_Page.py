from pageObjects.BasePage import BasePage
from pageObjects.TestCasePage import TestcasePage
from utilities.readProperties import ReadConfig
import time


class Test_TestCases():
    baseURL = ReadConfig.getApplicationURL()

    def test_testcases(self, setup1):
        self.driver = setup1
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.bp = BasePage(self.driver)
        self.bp.clickTestcases()

        self.tcp = TestcasePage(self.driver)
        self.tcp.getTestcasePageInfo()
        time.sleep(3)
