*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://www.practiceselenium.com/practice-form.html

*** Test Cases ***
Test_DropDownandListBox
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium speed  2seconds
    DropDownandListBox
    close browser


*** Keywords ***
DropDownandListBox
    select from list by label  continents  Asia
    sleep  3
    select from list by index  continents  5
    select from list by label  selenium_commands  Switch Commands
    select from list by label  selenium_commands  WebElement Commands
    unselect from list by label  selenium_commands  Switch Commands

