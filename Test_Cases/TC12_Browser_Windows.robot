*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://google.com
${url1}  http://bing.com

*** Test Cases ***
Test_BrowserWindows
    open browser  ${url}  ${browser}
    maximize browser window
    sleep  2

    open browser  ${url1}  ${browser}
    maximize browser window
    sleep  2

    switch browser  1
    ${title1}=  get title
    log to console  ${title1}

    switch browser  2
    ${title2}=  get title
    log to console  ${title2}

    close all browsers

*** Keywords ***