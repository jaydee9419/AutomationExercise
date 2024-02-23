import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\"+"config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def setUsername():
        uname = config.get('commonInfo', 'username')
        return uname

    @staticmethod
    def setMail():
        mail = config.get('commonInfo', 'mail')
        return mail

    @staticmethod
    def setPassword():
        password = config.get('commonInfo', 'password')
        return password

    @staticmethod
    def setFirstname():
        fname = config.get('commonInfo', 'fname')
        return fname

    @staticmethod
    def setLastname():
        lname = config.get('commonInfo', 'lname')
        return lname

    @staticmethod
    def setCompany():
        company = config.get('commonInfo', 'company')
        return company

    @staticmethod
    def setAddress():
        address = config.get('commonInfo', 'address')
        return address

    @staticmethod
    def setAddress2():
        address2 = config.get('commonInfo', 'address2')
        return address2

    @staticmethod
    def setState():
        state = config.get('commonInfo', 'state')
        return state

    @staticmethod
    def setCity():
        city = config.get('commonInfo', 'city')
        return city

    @staticmethod
    def setZipcode():
        zip_code = config.get('commonInfo', 'zipcode')
        return zip_code

    @staticmethod
    def setPhone():
        phone = config.get('commonInfo', 'phone')
        return phone

    @staticmethod
    def setDay():
        day = config.get('commonInfo', 'day')
        return day

    @staticmethod
    def setMonth():
        month = config.get('commonInfo', 'month')
        return month

    @staticmethod
    def setYear():
        year = config.get('commonInfo', 'year')
        return year
