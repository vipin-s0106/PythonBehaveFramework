import logging.config
import os
import re


class LogHandler:
    logger = None

    def __init__(self,file_path):
        conf_path = os.path.dirname(os.getcwd())+"\\config\\log_config.conf"

        #Setting the log file path to configuration file
        with open(conf_path,'r') as file:
            content = file.readlines()
            file_path = file_path.replace("\\", "\\\\")
            # print(file_path)
            for line_no in range(len(content)):
                if re.search("args=\('.*',", content[line_no]):
                    content[line_no] = "args=('" + file_path + "','a')\n"
                    break
        file.close()

        with open(conf_path,'w') as file:
            file.write(''.join(content))
        file.close()

        logging.config.fileConfig(conf_path)

        LogHandler.logger = logging.getLogger("root")

    @staticmethod
    def getLogger():
        return LogHandler.logger

