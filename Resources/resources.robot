*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Login
    [Arguments]  ${app_url}  ${app_browser}
    open browser  ${app_url}  ${app_browser}
    maximize browser window
    ${app_title}=  get title
    click link  xpath://a[@class='ico-login']
    input text  id:Email  pavanoltraining@gmail.com
    input text  id:Password  Test@123
    click element  xpath://input[@class='button-1 login-button']
    [Return]  ${app_title}