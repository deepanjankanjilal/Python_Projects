*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://swisnl.github.io/jQuery-contextMenu/demo.html
${url1}  https://testautomationpractice.blogspot.com/
${url2}  http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html

*** Test Cases ***
Test_Mouse_Opt
    open browser  ${url}  ${browser}
    maximize browser window
    sleep  2
    open context menu  xpath://span[@class='context-menu-one btn btn-neutral"
    sleep  2

    go to  ${url1}
    maximize browser window
    double click element  xpath://button[contains(text(), 'Copy Text')]
    sleep  2

    go to  ${url2}
    drag and drop  id:box6  id:box106
    sleep  5
    close browser

*** Keywords ***