*** Settings ***

Resource    RobotLibraries.robot
Resource    Variables.robot
Suite Setup     Create Session  SessionObject   ${base_url}
Test Template   EntryPoint for Request

*** Keywords ***
EntryPoint for Request
     [Arguments]  ${ActionName}  ${Execution}  ${Variable1}     ${Variable2}    ${Variable3}
     IF    $Execution == "Yes"
         Request    ${ActionName}  ${Variable1}     ${Variable2}    ${Variable3}
     END

Request
     [Arguments]    ${ActionName}   ${Variable1}     ${Variable2}    ${Variable3}

     ${DBConnection}=    convertExcelIntoDatabase    ${datafile}
     ${Actiontype}=      getActionType      ${DBConnection}     ${ActionName}
     IF    $Actiontype == "Get"
         Run Get Request    SessionObject  ${ActionName}    ${DBConnection}     ${Variable1}     ${Variable2}    ${Variable3}
     ELSE IF    $Actiontype == "Post"
          Run Post Request    SessionObject  ${ActionName}   ${Variables}
     
     ELSE IF    $Actiontype == "Put"
          Run Put Request    SessionObject  ${ActionName}   ${Variables}
     
     ELSE IF    $Actiontype == "Patch"
          Run Patch Request    SessionObject  ${ActionName}   ${Variables}
     
     ELSE IF    $Actiontype == "Delete"
          Run Delete Request    SessionObject  ${ActionName}   ${Variables}
          
     ELSE
         Log To Console    ${ActionType} is not found

     END

      releaseDbConnection   ${DBConnection}
      
*** Test Cases ***
EntryPoint for Request