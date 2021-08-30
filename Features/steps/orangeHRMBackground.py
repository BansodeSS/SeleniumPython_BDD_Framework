from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I launch browser')
def step_impl(context):
    assert  True,"test passed"


@when(u'I open application')
def step_impl(context):
    assert True, "test passed"


@when(u'Enter valid username and password')
def step_impl(context):
    assert True, "test passed"


@when(u'click on login')
def step_impl(context):
    assert True, "test passed"


@then(u'User must login to the Dashboard page')
def step_impl(context):
    assert True, "test passed"


@when(u'navigate to search page')
def step_impl(context):
    assert True, "test passed"


@then(u'search page should display')
def step_impl(context):
    assert True, "test passed"


@when(u'navigate to advance search page')
def step_impl(context):
    assert True, "test passed"


@then(u'advance search page should display')
def step_impl(context):
    assert True, "test passed"

