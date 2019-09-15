*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://demo.nopcommerce.com

*** Test Cases ***
Test_Login
    open browser  ${url}  ${browser}
    maximize browser window
    Login
    close browser


*** Keywords ***
Login
    click link  xpath://a[@class='ico-login']
    input text  id:Email  pavanoltraining@gmail.com
    input text  id:Password  Test@123
    click element  xpath://input[@class='button-1 login-button']