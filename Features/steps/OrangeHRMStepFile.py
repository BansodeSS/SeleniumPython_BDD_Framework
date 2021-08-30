from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given(u'launch chrome browser')
def launchBroswer(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'open ornage hrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@then(u'verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath('//*[@id="divLogo"]/img').is_displayed()
    assert status is True

@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
