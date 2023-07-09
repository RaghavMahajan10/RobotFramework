*** Settings ***
Library    String
*** Keywords ***

extract value from response
      [Arguments]   ${DBConnection}     ${ActionName}      ${json}

      @{variable}=   getEjectVariable    ${DBConnection}     ${ActionName}

      FOR    ${element}    IN    @{variable}
          @{list}=   Split String        ${element}     =
          ${Key}=   Set Variable    ${list}[0]
          ${path}=  Set Variable     ${list}[1]
       END
