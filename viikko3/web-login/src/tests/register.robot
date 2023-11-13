*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ronaldo
    Set Password  ronaldo123
    Set Password Confirmation  ronaldo123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ro
    Set Password  ronaldo123
    Set Password Confirmation  ronaldo123
    Submit Credentials
    Register Should Fail With Message  Username has to be atleast 3 characters long and contain characters from a-z


Register With Valid Username And Invalid Password
    Set Username  ronaldo
    Set Password  ronaldoronaldo
    Set Password Confirmation  ronaldoronaldo
    Submit Credentials
    Register Should Fail With Message  Password minumum length is 8 characters and can't only contain letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ronaldo
    Set Password  ronaldo1
    Set Password Confirmation  ronaldo2
    Submit Credentials
    Register Should Fail With Message  Password and Password confirmation don't match

Login After Successful Registration
    Set Username  ronaldo
    Set Password  ronaldo1
    Set Password Confirmation  ronaldo1
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Click Button  Logout
    Logout Should Succeed
    Set Username  ronaldo
    Set Password  ronaldo1
    Submit Credentials Login
    Login Should Succeed


Login After Failed Registration
    Set Username  ronaldo
    Set Password  ronaldo1
    Set Password Confirmation  ronaldo2
    Submit Credentials
    Register Should Fail With Message  Password and Password confirmation don't match
    Click Link  Login
    Set Username  ronaldo
    Set Password  ronaldo1
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Submit Credentials Login
    Click Button  Login

Logout Should Succeed
    Login Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}