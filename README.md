# Selenium Python BDD Framework
Behave tutorial

Setup
------------------
allure-behave
To Install allure-behave
 1) pip install allure-behave
 2) pycharm package

To execute test cases & generate report files( .json).
--------------------------------------------------
 behave -f allure_behave.formatter:AllureFormatter -o reports/ features

To Generate Allure report
--------------------------------------------
 allure serve reports/
