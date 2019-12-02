from behave import given,when,then
import time



@given(u'I navigated to the "{URL}" page')
def I_navigated_to_the_URL_page(context,URL):
    print(URL)


@given(u'I verified the "{URL}" page is opened')
def step_impl(context,URL):
    print(URL)


@given(u'I wait for "{2}" second')
def step_impl(context,wait_time):
    time.sleep(int(wait_time))


@when(u'I click on "{object}" with "{identifier}" "{value}"')
def step_impl(context,object,identifier,value):
    pass



@then(u'I verified "{object}" with "{identifier}" "{value}" present')
def step_impl(context,object,identifier,value):
    pass


@then(u'I take the screenshot with filename "{filename}"')
def step_impl(context,filename):
    pass

