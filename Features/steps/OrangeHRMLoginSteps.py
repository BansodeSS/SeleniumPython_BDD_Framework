from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given(u'I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'I open ornage hrm homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')

@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_id('txtUsername').send_keys(user)
    context.driver.find_element_by_id('txtPassword').send_keys(pwd)


@when(u'Click on the login Button')
def step_impl(context):
    context.driver.find_element_by_id('btnLogin').click()



@then(u'User must succesfully login to the Dashboard page')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
    assert text == "Dashboard"
    context.driver.close()

