*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://demowebshop.tricentis.com/register

*** Test Cases ***
Test_ImplicitWait
    open browser  ${url}  ${browser}
    maximize browser window
    set selenium implicit wait  10 seconds
    ImplicitWait_Test
    close browser


*** Keywords ***
ImplicitWait_Test
    select radio button  Gender  M
    input text  name:FirstName  David
    input text  name:LastName  John
    input text  name:Email  anhc@gmail.com
    input text  name:Password  davidjohn
    input text  name:ConfirmPassword  davidjohn
