from selenium.webdriver.common.by import By
import os
import time

class ContactUs():
    input_name_xpath = "//input[@placeholder='Name']"
    input_mail_xpath = "//input[@placeholder='Email']"
    input_subject_xpath = "//input[@placeholder='Subject']"
    input_message_xpath = "//textarea[@id='message']"
    input_file_xpath = "//input[@name='upload_file']"
    btn_submit_xpath = "//input[@name='submit']"
    txt_status_xpath = "//div[@class='status alert alert-success']"
    btn_home_xpath = "//a[normalize-space()='Home']"

    def __init__(self, driver):
        self.driver = driver

    def setMail(self, mail):
        self.driver.find_element(By.XPATH, self.input_mail_xpath).send_keys(mail)

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.input_name_xpath).send_keys(name)

    def setSubject(self):
        self.driver.find_element(By.XPATH, self.input_subject_xpath).send_keys("Hello")
    def setMessage(self):
        self.driver.find_element(By.XPATH, self.input_message_xpath).send_keys("World")

    def uploadFile(self):
        file = os.path.abspath(os.curdir)+"\\testdata\\myfile.pdf"
        self.driver.find_element(By.XPATH, self.input_file_xpath).send_keys(file)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()

    def getConfirmationMsg(self):
        try:
            status = self.driver.find_element(By.XPATH, self.txt_status_xpath).text
            print(status)
            return status
        except:
            print("Status message not found")

    def clickHome(self):
        self.driver.find_element(By.XPATH, self.btn_home_xpath).click()






