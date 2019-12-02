import os,configparser

class Settings:

    properties = None

    def __init__(self):
        current_path = os.path.dirname(os.getcwd())
        Settings.properties = configparser.RawConfigParser()
        Settings.properties.read(current_path+"\\GlobalSettings.properties")


    @staticmethod
    def getProperty():
        if Settings.properties == None:
            Settings()
        return Settings.properties