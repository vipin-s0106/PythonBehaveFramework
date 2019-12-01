from behave import given,when,then




@given(u'I navigated to the "{URL}" page')
def step_impl(context,URL):
    print(URL)


@given(u'I verified the "{URL}" page is opened')
def step_impl(context,URL):
    print(URL)


@when(u'I click on departure city dropdown')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on departure city dropdown')


@when(u'I click on "" with "text" "Boston"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "dropdown option" with "text" "Boston"')


@when(u'I click on destination city dropdown')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on destination city dropdown')


@when(u'I click on "dropdown option" with "text" "Dublin"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "dropdown option" with "text" "Dublin"')


@when(u'I click on "button" with "text" "Find Flights"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "button" with "text" "Find Flights"')


@then(u'I verified "object" with "text" "Flights from Boston to Dublin:" present')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I verified "object" with "text" "Flights from Boston to Dublin:" present')


@then(u'I take the screenshot with filename "image"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I take the screenshot with filename "image"')

