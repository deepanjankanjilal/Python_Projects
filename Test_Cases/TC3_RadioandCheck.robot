*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://www.practiceselenium.com/practice-form.html

*** Test Cases ***
Test_RadioandCheck
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium speed  2seconds
    RadioandCheck
    close browser


*** Keywords ***
RadioandCheck
    select radio button  sex  Female
    select radio button  exp  5
    select checkbox  BlackTea
    select checkbox  RedTea
    unselect checkbox  BlackTea
