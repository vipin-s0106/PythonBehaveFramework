import logging.config
import os
import re


class LogHandler:
    logger = None

    def __init__(self, filename):
        LogHandler.logger = logging.getLogger(__name__)

        # Create handlers
        f_handler = logging.FileHandler(filename,mode='w')
        f_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        f_format = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        LogHandler.logger.addHandler(f_handler)
        LogHandler.logger.info("working")


    @staticmethod
    def getInstance(filename):
        if LogHandler.logger is None:
            LogHandler(filename)
        return LogHandler.logger

    '''
    logger = None

    def __init__(self,file_path):
        conf_path = os.path.dirname(os.getcwd())+"\\config\\log_config.conf"

        #Setting the log file path to configuration file
        with open(conf_path,'r') as file:
            content = file.readlines()
        file.close()
        print(file_path)
        file_path = file_path.replace("\\","\\\\")
        print(file_path)
        for line_no in range(len(content)):
            if re.search("args=\('.*',",content[line_no]) != None:
                content[line_no] = re.sub("args=\('.*',",r"args=('"+file_path+"',",content[line_no])
                break
        with open(conf_path,'w') as file:
            file.writelines(content)
        file.close()

        logging.config.fileConfig(conf_path)

        LogHandler.logger = logging.getLogger(__name__)

        LogHandler.logger.info("Testing")

    @staticmethod
    def getLogger():
        return LogHandler.logger
    '''
