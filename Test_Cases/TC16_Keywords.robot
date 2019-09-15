*** Settings ***
Library  SeleniumLibrary
Library  SeleniumLibrary
Resource  ../Resources/resources.robot


*** Variables ***
${browser}  Chrome
${url}  http://demo.nopcommerce.com

*** Test Cases ***
Test_Login
    ${title}=  Login  ${url}  ${browser}
    log to console  ${title}
    log  ${title}
    close browser
