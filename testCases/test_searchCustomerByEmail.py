import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class Test_SearchCustomerByEmail_003:

    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() #Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self):

        self.logger.info("****************SearchCustomerByEmail_003***************************")
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

#Creating Login Page object lp
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successfully **********")

        self.logger.info("******* Starting Search Customer By Email **********")

#Creating SearchCustomerPage page object serachcust
        self.logger.info("************* Click in Customer Button **********")
        self.searchcust = SearchCustomerPage(self.driver)
        self.searchcust.clickOnCustomersMenu()
        self.searchcust.clickOnCustomersMenuItem()
        self.logger.info("************* Searching customer by emailID **********")
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickOnSearch()
        self.driver.implicitly_wait(6)
        status = self.searchcust.searchCustomerEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_003 Finished  *********** ")



