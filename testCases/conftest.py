import pytest
from selenium import webdriver

###########################################Pytest Browser Connectivity##########
#This function is used to pass command line argument during run
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
        browser_name = request.config.getoption("browser_name")

        if browser_name == "chrome":
                print("*************Launching Chrome browser******************")
                driver = webdriver.Chrome(
                                executable_path="C:\\Users\\prate\\Desktop\\PythonNotesRahulShetty\\ChromeDriver\\chromedriver.exe")
        elif browser_name == "firefox":
                print("*************Launching FireFox browser******************")
                driver = webdriver.Firefox(executable_path="C:\\Users\\prate\\Desktop\\PythonNotesRahulShetty\\FireFoxDriver\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        elif browser_name == "IE":
                print("IE")

        request.cls.driver = driver  # return the class driver through this line,so we can use driver object in another calling class
        yield
        driver.close()

###########################################Pytest HTML report##################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rashmi Ninawe'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)