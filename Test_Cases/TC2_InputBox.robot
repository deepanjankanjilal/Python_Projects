*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  Chrome
${url}  http://demo.nopcommerce.com

*** Test Cases ***
Test_InputBox
    open browser  ${url}  ${browser}
    maximize browser window
    Input_Box
    close browser


*** Keywords ***
Input_Box
    title should be  nopCommerce demo store
    click link  xpath://a[@class='ico-login']
    ${"email_txt"}  set variable  id:"Email"
    element should be visible  ${"email_txt"}
    element should be enabled  ${"email_txt"}
    input text  ${"email_txt"}  pavanoltraining@gmail.com
    sleep  5
    clear element text  ${"email_txt"}
    sleep  3
