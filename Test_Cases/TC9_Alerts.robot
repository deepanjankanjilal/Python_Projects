*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://testautomationpractice.blogspot.com/

*** Test Cases ***
Test_Alerts
    open browser  ${url}  ${browser}
    maximize browser window
    click element  xpath://*[@id="HTML9"]/div[1]/button
    sleep  3
    handle alert  accept
    handle alert  dismiss
    handle alert  leave
    alert should be present  Press a button


*** Keywords ***