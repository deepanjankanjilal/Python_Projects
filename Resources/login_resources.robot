*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://admin-demo.nopcommerce.com
${browser}  Chrome

*** Keywords ***
Open my Browser
    open browser  ${url}  ${browser}
    maximize browser window

Close Browser
    close all browsers

Open Login Page
    go to  ${url}

Input username
    [Arguments]  ${username}
    input text  id:Email  ${username}

Input pwd
    [Arguments]  ${password}
    input text  id:Password  ${password}

click login button
    click element  xpath://input[@class='button-1 login-button']

click logout link
    click link  Logout

Error message should be visible
    page should contain  Login was unsuccessful

Dashboard page should be visible
    page should contain  Dashboard