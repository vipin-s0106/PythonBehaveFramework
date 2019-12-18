from datetime import datetime
import os
import sys

#Adding all the Path to system path so that everthing can be accessible in each module
path = os.getcwd()
print(path)
sys.path.append(path+"\\")
sys.path.append(path+"\\Features\\")

#importing the module
from src.framework.LogHandler import LogHandler
from Features.GlobalVariable import global_dict

#Creating Timestamp Folder
path = os.getcwd()+"\\output"
current_timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
output_path = os.path.join(path,current_timestamp)
os.makedirs(output_path)


#Configuring the Logger
LogHandler(os.path.join(output_path,"output.log"))
logger = LogHandler.getLogger()

#Don't move the below import statement
from Features.steps.BaseClass import BaseClass
from src.framework.WebDriverFactory import WebDriverFactory

def before_all(context):
    # String output Folder Path to Global Variable so that it can be access in each module
    global_dict["output_path"] = output_path

    #Configuring the Behave framework
    logger.info("Configuring the behave framework")
    BaseClass()


def after_all(context):
    WebDriverFactory.closeBrowser()








