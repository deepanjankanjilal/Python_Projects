*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://seleniumhq.github.io/selenium/docs/api/java/index

*** Test Cases ***
Test_Frames
    open browser  ${url}  ${browser}
    maximize browser window
    select frame  packageListFrame
    click link  org.openqa.selenium
    unselect frame
    sleep  3

    select frame  packageFrame
    click link  WebDriver
    unselect frame
    sleep  3

    select frame  classFrame
    click link  Help
    unselect frame
    close browser

*** Keywords ***