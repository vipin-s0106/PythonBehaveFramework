from behave import given,when,then
import time
from Features.GlobalVariable import global_dict
from Features.steps.BaseClass import BaseClass


from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()


@given(u'I navigated to the "{URL}" page')
def I_navigated_to_the_URL_page(context,URL):
    BaseClass.common.navigate(BaseClass.properties.get("URL",URL))
    logger.info("Navigating to - "+URL)


@given(u'I verified the "{URL}" page is opened')
def step_impl(context,URL):
    pass

@given(u'I wait for "{wait_time}" second')
def step_impl(context,wait_time):
    print("Waitng ")
    time.sleep(int(wait_time))


@when(u'I click on "{object}" with "{identifier}" "{value}"')
def step_impl(context,object,identifier,value):
    print("12")
    BaseClass.common.click(object,identifier,value)



@then(u'I verified "{object}" with "{identifier}" "{value}" present')
def step_impl(context,object,identifier,value):
    pass


@then(u'I take the screenshot with filename "{filename}"')
def step_impl(context,filename):
    pass

