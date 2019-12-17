from Features.GlobalVariable import global_dict

from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()

from src.framework.DatabaseConnectionFactory import DatabaseConnectionFactory
from src.framework.Settings import Settings
from src.utils.pyrobot import Robot
from src.po.AbstractClass import AbstractClass
from src.utils.Common import Common


class BaseClass:
    connection = None
    properties = None
    robot = None
    common = None

    def __init__(self):
        logger.info("Configuring the Base Class")
        AbstractClass()
        BaseClass.properties = Settings.getProperty()
        BaseClass.connection = DatabaseConnectionFactory.get_connection("ORACLE")
        BaseClass.robot = Robot()
        BaseClass.common = Common()
