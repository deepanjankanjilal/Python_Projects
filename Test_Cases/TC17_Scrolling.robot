*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  https://www.countries-ofthe-world.com/flags-of-the-world.html

*** Test Cases ***
Test_Scroll
    open browser  ${url}  ${browser}
    maximize browser window
    execute javascript  window.scrollTo(0,2500)
    sleep  2
    scroll element into view  xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]
    execute javascript  window.scrollTo(0,document.body.scrollHeight)
    close browser


*** Keywords ***