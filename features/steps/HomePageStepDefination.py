from behave import given,when,then
from features.GlobalVariable import global_dict
from features.steps.BaseClass import BaseClass


from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()


@when(u'I click on departure city dropdown')
def step_impl(context):
    BaseClass.home_page.click_departure_city_dropdown()


@when(u'I click on destination city dropdown')
def step_impl(context):
    BaseClass.home_page.click_destination_city_dropdown()
