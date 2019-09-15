*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://google.com
${url1}  http://bing.com

*** Test Cases ***
Test_Navig_Keywrd
    open browser  ${url}  ${browser}
    maximize browser window
    ${loc1}=  get location
    log to console  ${loc1}
    go to  ${url1}
    ${loc2}=  get location
    log to console  ${loc2}
    go back
    ${loc3}=  get location
    log to console  ${loc3}
    close all browsers

*** Keywords ***