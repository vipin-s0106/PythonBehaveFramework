from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()

class CSVReporting:

    report_dict = {}
    testcase_id = ""
    @staticmethod
    def CreateCSVReport(filepath):
        if (len(CSVReporting.report_dict)) != 0:
            for key,value in CSVReporting.report_dict.items():
                with open(filepath,"a+") as file:
                    file.write(str(key)+", "+str(value)+"\n")
                file.close()
        else:
            logger.info("CSV report can't be generate as No testcase ID found to generate the report")