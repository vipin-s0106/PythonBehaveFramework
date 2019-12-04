from src.framework.WebDriverFactory import WebDriverFactory
from src.framework.DatabaseConnectionFactory import DatabaseConnectionFactory
from src.framework.LogHandler import LogHandler
import logging


# LogHandler("C:\\Users\\vipin\\PycharmProjects\\PythonBehaveFramework\\output\\output.log")
LogHandler.getInstance("C:\\Users\\vipin\\PycharmProjects\\PythonBehaveFramework\\output\\output.log")

logger = logging.getLogger(__name__)
logger.info("logger")