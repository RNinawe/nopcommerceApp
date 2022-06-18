import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class Test_SerchCustomerByName:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName_004(self):
        self.logger.info("****************SearchCustomerByName_004***************************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

#Creating Login Page object lp
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successfully **********")
        self.logger.info("******* Starting Search Customer By Name **********")

#Creating SearchCustomerPage page object searchcust
        self.logger.info("************* Click in Customer Button **********")
        self.searchcust = SearchCustomerPage(self.driver)
        self.searchcust.clickOnCustomersMenu()
        self.searchcust.clickOnCustomersMenuItem()
        self.logger.info("************* Searching customer by Name **********")
        self.searchcust.setFirstName("Victoria")
        self.searchcust.setLastName("Terces")
        self.searchcust.clickOnSearch()
        self.driver.implicitly_wait(6)
        status = self.searchcust.searchCustomerName("Victoria Terces")
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_004 Finished  *********** ")






