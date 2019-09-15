*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://testautomationpractice.blogspot.com

*** Test Cases ***
Test_Links
    open browser  ${url}  ${browser}
    maximize browser window
    ${tbl_row}=  get element count  xpath://table[@name='BookTable']/tbody/tr
    ${tbl_col}=  get element count  xpath://table[@name='BookTable']/tbody/tr[1]/th
    log to console  ${tbl_row}
    log to console  ${tbl_col}

    # Get data from specific column
    ${dat_text}=  get text  xpath://table[@name='BookTable']/tbody/tr[5]/td[1]
    log to console  ${dat_text}

    # Validate contents of HTML table
    table column should contain  xpath://table[@name='BookTable']  2  Author
    table row should contain  xpath://table[@name='BookTable']  4  Learn JS
    table cell should contain  xpath://table[@name='BookTable']  5  2  Mukesh
    table header should contain  xpath://table[@name='BookTable']  BookName
    close browser


*** Keywords ***