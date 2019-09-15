*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://demowebshop.tricentis.com/register

*** Test Cases ***
Test_SpeedTest
    ${bef_speed}=  get selenium speed
    log to console  ${bef_speed}
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium speed  2 seconds
    Speed_Test
    close browser


*** Keywords ***
Speed_Test
    select radio button  Gender  M
    input text  name:FirstName  David
    input text  name:LastName  John
    input text  name:Email  anhc@gmail.com
    input text  name:Password  davidjohn
    input text  name:ConfirmPassword  davidjohn
    ${aft_speed}=  get selenium speed
    log to console  ${aft_speed}
