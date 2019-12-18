from behave import given,when,then
import time
from Features.GlobalVariable import global_dict
from Features.steps.BaseClass import BaseClass


from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()


@given(u'I navigated to the "{URL}" page')
def step_impl(context,URL):
    BaseClass.common.navigate(BaseClass.properties.get("URL",URL))
    logger.info("Navigating to - '"+BaseClass.properties.get("URL",URL)+"'")


@given('I verified the "{URL}" page is opened')
def step_impl(context,URL):
    url = BaseClass.common.getCurrentURL()
    assert url == BaseClass.properties.get("URL",URL)
    logger.info("URL '"+BaseClass.properties.get("URL",URL)+"' is verified")


@given(u'I wait for "{wait_time}" second')
def step_impl(context,wait_time):
    time.sleep(int(wait_time))
    logger.info("Waiting for " + wait_time + " second")


@when(u'I wait for "{wait_time}" second')
def step_impl(context,wait_time):
    time.sleep(int(wait_time))
    logger.info("Waiting for " + wait_time + " second")


@then(u'I wait for "{wait_time}" second')
def step_impl(context,wait_time):
    time.sleep(int(wait_time))
    logger.info("Waiting for " + wait_time)



@when(u'I click on "{object}" with "{identifier}" "{value}"')
def step_impl(context,object,identifier,value):
    BaseClass.common.click(object,identifier,value)
    time.sleep(2)
    logger.info("I click on '" + object + "' with '" + identifier + "' '" + value+"'")


@then(u'I click on "{object}" with "{identifier}" "{value}"')
def step_impl(context,object,identifier,value):
    BaseClass.common.click(object,identifier,value)
    time.sleep(2)
    logger.info("I click on '" + object + "' with '" + identifier + "' '" + value+"'")


@then(u'I verified "{object}" with "{identifier}" "{value}" present')
def step_impl(context,object,identifier,value):
    status = BaseClass.common.verifyObject(object,identifier,value)
    assert status == True
    logger.info("I verified '"+object+"' with '"+identifier+"' '"+value+"' present")


@when(u'I take the screenshot with filename "{filename}"')
def step_impl(context,filename):
    BaseClass.common.takeScreenShot(global_dict["output_path"]+"\\"+filename)
    logger.info("I take the screenshot with filename "+filename)


@then(u'I take the screenshot with filename "{filename}"')
def step_impl(context,filename):
    BaseClass.common.takeScreenShot(global_dict["output_path"]+"\\"+filename)
    logger.info("I take the screenshot with filename "+filename)

