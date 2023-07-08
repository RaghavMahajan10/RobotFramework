*** Settings ***
Resource  RobotLibraries.robot

*** Keywords ***
Run Get Request
    [Arguments]   ${sessionObject}  ${ActionName}   ${DBConnection}   @{variables}

    ${Endpoint}=   getEndpoint     ${DBConnection}     ${ActionName}
    ${Response}=   get on session    ${sessionObject}  ${Endpoint}

    ${ExpectedStatusCode}=      getResponseCode     ${DBConnection}     ${ActionName}
    
    Should Be Equal    ${ExpectedStatusCode}    ${Response.status_code}

#Run Post Request
#    [Arguments]
#
#
#Run Put Request
#    [Arguments]
#
#
#Run Patch Request
#    [Arguments]
#
#Run Delete Request
#    [Arguments]