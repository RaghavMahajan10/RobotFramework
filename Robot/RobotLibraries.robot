*** Settings ***

Library  RequestsLibrary
Library  Collections
Library    DataDriver  file=../Resources/TestCaseFiles/flow.xlsx  sheet_name=Testcases
Library  OperatingSystem
Library     String
Library  JSONLibrary
Library     ../Utilites/DataReader.py
Resource    ApiMethods.robot
Resource    Variables.robot
Resource    EjectVariable.robot