from behave import given,when,then
from Features.GlobalVariable import global_dict
from Features.steps.BaseClass import BaseClass

from src.framework.LogHandler import LogHandler
logger = LogHandler.getLogger()


@given(u'I click on "{button}" with "{text}" "{FindFlights}"')
def step_impl(context,button,text,FindFlights):
    print("FindFlights")
    BaseClass.common.click(button,text,"Find Flights")





@when(u'I click on departure city dropdown')
def step_impl(context):
    pass


@when(u'I click on destination city dropdown')
def step_impl(context):
    pass
