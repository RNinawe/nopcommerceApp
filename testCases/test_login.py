import pytest
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class Test_Login_001(BaseClass):

#Reading data from readproperties.py file
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

#Passed loggen object in logger variable
    logger = LogGen.loggen()

#Checking HOMEPAGE
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePagetitle(self):
        self.logger.info("****************Verifying test_home Page title TC**************************")
        self.logger.info("**************Verifying Home Page Title********************")
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        #Checking tile of HomePage
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("*************Home Page Title is PASSED********************")
        else:
            self.driver.save_screenshot("C:\\Users\prate\\PycharmProjects\\nopcommerceApp\\ScreenShots\\" + "test_homePagetitle.png")
            self.logger.info("*************Home Page Title is FAILED********************")
            assert False

#Checking Login Page
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("****************Verifying test_login TC**************************")
        self.logger.info("**************Verifying Login Page Title********************")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        #Checking tile after login into page
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************Login Page Title is PASSED********************")
        else:
            self.driver.save_screenshot(
                "C:\\Users\prate\\PycharmProjects\\nopcommerceApp\\ScreenShots\\" + "test_login.png")
            self.logger.info("*************Login Page Title is FAILED********************")
            assert False