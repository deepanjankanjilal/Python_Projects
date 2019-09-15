*** Settings ***
Library  SeleniumLibrary

Resource  ../Resources/login_resources.robot
Library  DataDriver  E:/Pycharm_Projects/Robot/TestData/LoginData.xlsx

Suite Setup  Open my browser
Suite Teardown  Close Browser
Test Template  Invalid login


*** Test Cases ***
LoginTestwithExcel using  ${username}   ${password}


*** Keywords ***
Invalid login
    [Arguments]  ${username}  ${password}
    Input username  ${username}
    Input pwd  ${password}
    click login button
    Error message should be visible
