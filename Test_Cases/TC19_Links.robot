*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://www.newtours.demoaut.com/

*** Test Cases ***
Test_Links
    open browser  ${url}  ${browser}
    maximize browser window
    ${tot_lnk}=  get element count  xpath://a
    log to console  {tot_lnk}

    @{lnk_items}  create list

    : FOR  ${i}  IN RANGE  1  ${tot_lnk}
    \  ${lnk_txt}=  get text  xpath:(//a)[${i}]
    \  log to console  ${lnk_txt}
    close browser


*** Keywords ***