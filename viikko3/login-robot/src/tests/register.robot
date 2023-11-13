*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ronaldo  ronaldo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  ronaldo123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ro  ronaldo123
    Output Should Contain  Username has to be atleast 3 characters long and contain characters from a-z

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  ""ronaldo  ronaldo123
    Output Should Contain  Username has to be atleast 3 characters long and contain characters from a-z

Register With Valid Username And Too Short Password
    Input Credentials  ronaldo  ro123
    Output Should Contain  Password minumum length is 8 characters and has to contain a letter and number

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ronaldo  RoNaLDOOOO
    Output Should Contain  Password minumum length is 8 characters and has to contain a letter and number

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command