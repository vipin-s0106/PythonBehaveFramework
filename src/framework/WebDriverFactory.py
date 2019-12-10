from src.framework.Settings import Settings
import os
from selenium import webdriver
import traceback


class WebDriverFactory:
    #creating the static driver
    driver = None
    __initialised = False

    @staticmethod
    def get_driver():
        if WebDriverFactory.__initialised  == False:
            WebDriverFactory.sharedDriver()
        return WebDriverFactory.driver

    @staticmethod
    def sharedDriver():
        try:
            #getting the properties file object
            properties = Settings.getProperty()
            browser = properties.get("SETUP","BROWSER")
            print("Automation execution started on "+browser+" browser")

            current_path = os.path.dirname(os.getcwd())

            if browser.upper() == "INTERNET EXPLORER":
                internet_explorer_driver_path = current_path+"\\Driver\\IEDriverServer.exe"
                os.environ["webdriver.ie.driver"] = internet_explorer_driver_path

                # setting Options
                options = webdriver.IeOptions()
                options.ignore_protected_mode_settings = True
                options.ignore_zoom_level = True

                WebDriverFactory.driver = webdriver.Ie(executable_path=internet_explorer_driver_path,options=options)

            elif browser.upper() == "CHROME":
                #disabling all the chrome extension
                options = webdriver.ChromeOptions()
                options.add_argument("--disable-extensions")

                chrome_driver_path = current_path+"\\Driver\\chromedriver.exe"
                os.environ["webdriver.chrome.driver"] = chrome_driver_path

                #creating the chromedriver object
                WebDriverFactory.driver = webdriver.Chrome(executable_path=chrome_driver_path,options=options)

            else:
                raise Exception(browser+" driver is not supported by the framework")

            '''
            =============== Some Basic Settings ============
            '''
            WebDriverFactory.driver.maximize_window()

            # setting for each element to wait in seconds
            WebDriverFactory.driver.implicitly_wait(10)
            WebDriverFactory.__initialised = True
        except Exception as e:
            traceback.print_stack()
            print(str(e))


    @staticmethod
    def closeBrowser():
        WebDriverFactory.driver.quit()
        WebDriverFactory.__initialised = False
