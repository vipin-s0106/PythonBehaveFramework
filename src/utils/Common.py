from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.framework.WebDriverFactory import WebDriverFactory
import traceback
from selenium.webdriver.common.action_chains import ActionChains


class Common:

    driver = None
    wait = None
    action = None

    def __init__(self):
        Common.driver = WebDriverFactory.get_driver()
        Common.wait = WebDriverWait(Common.driver,20)
        Common.action = ActionChains(Common.driver)


    def navigate(self,URL):
        try:
            Common.driver.get(URL)
        except Exception as e:
            print("Not able to navigate to "+URL)
            print(traceback.print_stack())


    def click(self,object,identifier,value):
        try:
            if identifier.lower() == "id":
                Common.driver.find_element_by_id(value).click()
            elif identifier.lower() == "name":
                Common.driver.find_element_by_name(value).click()
            elif identifier.lower() == "linktext":
                Common.driver.find_element_by_link_text(value).click()
            elif identifier.lower() == "partial_linktext":
                Common.driver.find_element_by_partial_link_text(value).click()
            elif identifier.lower() == "text":
                xpath = "//*[text()='"+value+"']"
                Common.driver.find_element_by_xpath(xpath).click()
            elif identifier.lower() == "xpath":
                Common.driver.find_element_by_xpath(value).click()
            else:
                raise Exception("Invalid Identifier - "+identifier)
        except Exception as e:
            print("Not able to click on "+str(object)+" using identifier "+identifier+" with value "+value)
            print(traceback.print_stack())




    def type(self,object,identifier,value,text):
        try:
            if identifier.lower() == "id":
                Common.driver.find_element_by_id(value).send_keys(text)
            elif identifier.lower() == "name":
                Common.driver.find_element_by_name(value).send_keys(text)
            elif identifier.lower() == "class":
                Common.driver.find_element_by_class_name(value).send_keys(text)
            elif identifier.lower() == "xpath":
                Common.driver.find_element_by_xpath(value).send_keys(text)
            else:
                raise Exception("Invalid Identifier - "+identifier)
        except Exception as e:
            print("Not able to enter text for "+str(object)+" using identifier "+identifier+" with value "+value)
            print(traceback.print_stack())



    def doubleClick(self,object,identifier,value):
        try:
            if identifier.lower() == "id":
                element = Common.driver.find_element_by_id(value)
            elif identifier.lower() == "name":
                element = Common.driver.find_element_by_name(value)
            elif identifier.lower() == "class":
                element = Common.driver.find_element_by_class_name(value)
            elif identifier.lower() == "text":
                xpath = "//*[text()='"+value+"']"
                element = Common.driver.find_element_by_xpath(xpath)
            elif identifier.lower() == "xpath":
                element = Common.driver.find_element_by_xpath(value)
            else:
                raise Exception("Invalid Identifier - "+identifier)

            Common.action.double_click(element).perform()

        except Exception as e:
            print("Not able to double click for "+str(object)+" using identifier "+identifier+" with value "+value)
            print(traceback.print_stack())



    def verifyObject(self,object,identifier,value):
        try:
            if identifier.lower() == "id":
                elements = Common.driver.find_elements_by_id(value)
            elif identifier.lower() == "name":
                elements = Common.driver.find_elements_by_name(value)
            elif identifier.lower() == "class":
                elements = Common.driver.find_elements_by_class_name(value)
            elif identifier.lower() == "text":
                xpath = "//*[text()='" + value + "']"
                elements = Common.driver.find_elements_by_xpath(xpath)
            elif identifier.lower() == "xpath":
                elements = Common.driver.find_elements_by_xpath(value)
            else:
                raise Exception("Invalid Identifier - "+identifier)

            if len(elements) >= 1:
                return True
            return False

        except Exception as e:
            print("Not able to verify "+str(object)+" using identifier "+identifier+" with value "+value)
            print(traceback.print_stack())




    def rightClick(self,object1,identifier1,value1,object2,identifier2,value2):
        try:
            if identifier1.lower() == "id":
                RightClikableelement = Common.driver.find_element_by_id(value1)
            elif identifier1.lower() == "name":
                RightClikableelement = Common.driver.find_element_by_name(value1)
            elif identifier1.lower() == "class":
                RightClikableelement = Common.driver.find_element_by_class_name(value1)
            elif identifier1.lower() == "text":
                xpath = "//*[text()='"+value1+"']"
                RightClikableelement = Common.driver.find_element_by_xpath(xpath)
            elif identifier1.lower() == "xpath":
                RightClikableelement = Common.driver.find_element_by_xpath(value1)
            else:
                raise Exception("Invalid Identifier - "+identifier1)

            Common.action.context_click(RightClikableelement).perform()

            element_xpath = "//*[text()='"+value2+"']"
            Common.driver.find_element_by_xpath(element_xpath)

        except Exception as e:
            print("Not able to double click for "+str(object1)+" using identifier "+identifier1+" with value "+value1)
            print(traceback.print_stack())



    def getCurrentURL(self):
        try:
            return Common.driver.current_url
        except Exception as e:
            print(traceback.print_stack())


    def getTitle(self):
        try:
            return Common.driver.title
        except Exception as e:
            print(traceback.print_stack())


    def SwitchToFrame(self,identifier,value):
        try:
            if identifier.lower() == "id":
                element = Common.driver.find_element_by_id(value)
            elif identifier.lower() == "name":
                element = Common.driver.find_element_by_name(value)
            elif identifier.lower() == "class":
                element = Common.driver.find_element_by_class_name(value)
            elif identifier.lower() == "xpath":
                element = Common.driver.find_element_by_xpath(value)
            else:
                raise Exception("Invalid Identifier - " + identifier)

            Common.driver.switch_to.frame(element)

        except Exception as e:
            print("Not able to switch frame for identifier " + identifier + " with value " + value)
            print(traceback.print_stack())



    def SwitchToMainFrame(self):
        try:
            Common.driver.default_content()
        except Exception as e:
            print(traceback.print_stack())


    def getElementText(self,object,identifier,value):
        try:
            if identifier.lower() == "id":
                element = Common.driver.find_element_by_id(value)
            elif identifier.lower() == "name":
                element = Common.driver.find_element_by_name(value)
            elif identifier.lower() == "class":
                element = Common.driver.find_element_by_class_name(value)
            elif identifier.lower() == "text":
                xpath = "//*[text()='" + value + "']"
                element = Common.driver.find_element_by_xpath(xpath)
            elif identifier.lower() == "xpath":
                element = Common.driver.find_element_by_xpath(value)
            else:
                raise Exception("Invalid Identifier - "+identifier)

            return element.text

        except Exception as e:
            print("Not able to find "+str(object)+" using identifier "+identifier+" with value "+value)
            print(traceback.print_stack())


    def takeScreenShot(self,filepath):
        try:
            fileprefix = filepath.split(".")[-1]
            if fileprefix in ["jpg","png","jpeg"]:
                Common.driver.save_screenshot(filepath)
            else:
                raise Exception("Invalid File Format - "+fileprefix)
        except Exception as e:
            print("Not able to take the screenshot")
            print(traceback.print_stack())