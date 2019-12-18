from src.po.AbstractClass import AbstractClass
import time

from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()

class HomePage(AbstractClass):

    #######################################################################
    departure_city_dropdown_xpath = "//*[@name='fromPort']"
    destination_city_dropdown_xpath = "//*[@name='toPort']"





    #######################################################################


    def click_departure_city_dropdown(self):
        AbstractClass.driver.find_element_by_xpath(HomePage.departure_city_dropdown_xpath).click()
        time.sleep(2)
        logger.info("Click on departure city dropdown")

    def click_destination_city_dropdown(self):
        AbstractClass.driver.find_element_by_xpath(HomePage.destination_city_dropdown_xpath).click()
        time.sleep(2)
        logger.info("Click on destination city dropdown")
