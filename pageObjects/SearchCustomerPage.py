from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    textEmail_id = "SearchEmail"
    textFirstName_id = "SearchFirstName"
    textLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    textFirstName_id = "SearchFirstName"
    tblEmailsRows_xpath = "//table[@class='table table-bordered table-hover table-striped dataTable no-footer']//td[2]"
    tblNamesRows_xpath = "//table[@class='table table-bordered table-hover table-striped dataTable no-footer']//td[3]"

#Action Methods
    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.textEmail_id).clear()
        self.driver.find_element(By.ID,self.textEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.textFirstName_id).clear()
        self.driver.find_element(By.ID,self.textFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.textLastName_id).clear()
        self.driver.find_element(By.ID,self.textLastName_id).send_keys(lname)

    def clickOnSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def searchCustomerEmail(self,email):
        flag = False
        emails = self.driver.find_elements(By.XPATH, self.tblEmailsRows_xpath)

        for i in emails:
            if email in i.text:
                flag = True
                print("Email ID is Present in Table list")
                break
            else:
                print("Email ID is not Present in Table list")
        return flag

    def searchCustomerName(self,name):
        flag = False
        Names = self.driver.find_elements(By.XPATH, self.tblNamesRows_xpath)

        for i in Names:
            if name in i.text:
                flag=True
                break
            else:
                print("Name is not Present in Table list")
        return flag


        return flag

