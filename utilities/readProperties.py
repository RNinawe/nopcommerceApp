#Through this file we are reading file from condif.ini
#We have to import configparser pacakge so we can use its functions
#We have to create separte functions for all var present on configini
#We have to crate all method/function as static so we can called this directly by class name
import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\prate\\PycharmProjects\\nopcommerceApp\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserEmail():
        useremail=config.get('common info','useremail')
        return useremail

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

