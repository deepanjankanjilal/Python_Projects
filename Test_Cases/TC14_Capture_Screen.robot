*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://opensource-demo.orangehrmlive.com/

*** Test Cases ***
Test_Capture_Screen
    open browser  ${url}  ${browser}
    maximize browser window
    input text  id:txtUsername  Admin
    input text  id:txtPassword  admin123
    sleep  1
    capture element screenshot  xpath://*[@id="divLogo"]/img  E:/Pycharm_Projects/Robot/logo.png
    capture page screenshot  E:/Pycharm_Projects/Robot/page.png
    close all browsers

*** Keywords ***