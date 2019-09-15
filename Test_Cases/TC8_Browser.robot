*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://localhost/phpmyadmin/tbl_structure.php?db=test&table=demo_table
${browser1}  Chrome
${url1}  http://localhost/phpmyadmin/tbl_structure.php?db=test&table=customer

*** Test Cases ***
Test_Browser
    open browser  ${url}  ${browser}
    maximize browser window
    open browser  ${url1}  ${browser1}
    maximize browser window
    #close browser
    close all browsers


*** Keywords ***