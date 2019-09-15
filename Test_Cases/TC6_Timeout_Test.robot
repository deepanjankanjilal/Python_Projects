*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://demowebshop.tricentis.com/register

*** Test Cases ***
Test_TimeoutTest
    open browser  ${url}  ${browser}
    maximize browser window
    ${time_bef}=  get selenium timeout
    log to console  ${time_bef}
    set selenium timeout  10 seconds
    wait until page contains  Register
    Timeout_Test
    close browser


*** Keywords ***
Timeout_Test
    select radio button  Gender  M
    input text  name:FirstName  David
    input text  name:LastName  John
    input text  name:Email  anhc@gmail.com
    input text  name:Password  davidjohn
    input text  name:ConfirmPassword  davidjohn
    ${time_aft}=  get selenium timeout
    log to console  ${time_aft}
