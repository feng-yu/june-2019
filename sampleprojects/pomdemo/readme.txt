This the project to demo the POM (Page Object Model) and Selenium.

The good tutorial is at:  https://www.youtube.com/watch?v=BURK7wMcCwU

It uses:
1. POM (Page Object Model)
2. Selenium
3. Python Unit Test (unittest)
4. HTML (html-testRunner)

The example app is at:
https://opensource-demo.orangehrmlive.com

To run the test from command line: (using -m option and file name wihtout .py extension)
c:\Users\User\PycharmProjects\june-2019>python -m sampleprojects.pomdemo.tests.TestLoginPage

To get the html report:
1. unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/User/PycharmProjects/june-2019/sampleprojects/pomdemo/reports'))
2. Has to run from command line as:
    c:\Users\User\PycharmProjects\june-2019>python -m sampleprojects.pomdemo.tests.TestLoginPage
   Run from pycharm, doesn't generate the html report