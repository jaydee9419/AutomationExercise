from selenium.webdriver.common.by import By

class TestcasePage():
    txt_testcase_xpath = "//b[normalize-space()='Test Cases']"

    def __init__(self, driver):
        self.driver = driver

    def getTestcasePageInfo(self):
        try:
            testcase_page = self.driver.find_element(By.XPATH, self.txt_testcase_xpath).text
            print(testcase_page)
            return testcase_page
        except:
            print("Unable to find the testcase page element")
