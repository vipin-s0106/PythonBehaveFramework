from src.framework.WebDriverFactory import WebDriverFactory
from src.framework.Settings import Settings
from src.framework.DatabaseConnectionFactory import DatabaseConnectionFactory
from src.utils.pyrobot import Robot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()



class AbstractClass:
    driver = None
    wait = None
    properties = None
    connection = None
    robot = None


    def __init__(self):
        AbstractClass.driver = WebDriverFactory.get_driver()
        AbstractClass.wait = WebDriverWait(AbstractClass.driver,20)
        AbstractClass.properties = Settings.getProperty()
        AbstractClass.connection = DatabaseConnectionFactory.get_connection("oracle")
        AbstractClass.robot = Robot()
