from selenium.webdriver.common.by import By


class Login():
    txt_loginpage_xpath = "//h2[normalize-space()='Login to your account']"
    input_email_xpath = "//input[@data-qa='login-email']"
    input_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[normalize-space()='Login']"

    txt_newuser_xpath = "//h2[normalize-space()='New User Signup!']"
    input_uname_xpath = "//input[@placeholder='Name']"
    imput_email_xpath = "//input[@data-qa='signup-email']"
    btn_signup_xpath = "//button[normalize-space()='Signup']"
    txt_signupfailed_xpath = "//p[normalize-space()='Email Address already exist!']"

    txt_deleteconfmsg_xpath = "//b[normalize-space()='Account Deleted!']"

    txt_loginfailmsg_xpath = "//p[normalize-space()='Your email or password is incorrect!']"


    def __init__(self, driver):
        self.driver = driver

    def checkNewuserPageVisability(self):
        try:
            newuser_text = self.driver.find_element(By.XPATH, self.txt_newuser_xpath).text
            return newuser_text
        except:
            print("New user page not visible")

    def getConfMsg(self):
        try:
            login_page_msg = self.driver.find_element(By.XPATH, self.txt_loginpage_xpath).text
            print(login_page_msg)
            return login_page_msg
        except:
            print("Unable to find the login page text")

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def getDeleteconfMsg(self):
        try:
            delete_msg = self.driver.find_element(By.XPATH, self.txt_deleteconfmsg_xpath).text
            print(delete_msg)
            return delete_msg
        except:
            print("Unable to find the deleted confirmed msg")

    def getLoginFailedMsg(self):
        try:
            login_failed = self.driver.find_element(By.XPATH, self.txt_loginfailmsg_xpath).text
            print("Error:", login_failed)
            return login_failed
        except:
            print("Unable to find the login failed msg")

    def setName(self, uname):
        try:
            user = self.driver.find_element(By.XPATH, self.input_uname_xpath).send_keys(uname)
            return user
        except:
            pass

    def setMail(self, email):
        self.driver.find_element(By.XPATH, self.imput_email_xpath).send_keys(email)

    def clickSignup(self):
        self.driver.find_element(By.XPATH, self.btn_signup_xpath).click()

    def getSignupFailedMsg(self):
        try:
            signup_failed = self.driver.find_element(By.XPATH, self.txt_signupfailed_xpath).text
            print("Error:", signup_failed)
            return signup_failed
        except:
            print("Unable to find the signup failed msg")
