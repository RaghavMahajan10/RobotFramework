import sqlite3

import pandas as pd


def convertExcelIntoDatabase(excelFile):
    try:
        db = sqlite3.connect('sqlite.db')
        dfs = pd.read_excel(excelFile, engine='openpyxl', sheet_name=None)
        for workflow, df in dfs.items():
            df.to_sql(workflow, db, if_exists='replace')
            print(f'{df} inserted successfully')
        return db
    except Exception as e:
        print("Error")


def releaseDbConnection(db):
    try:
        db.close()
        print("dataconnection closed")
    except:
        print("Error while closing file")


def getActionType(db, actionName):
    try:

        cursor = db.cursor()
        sqlQuery = 'SELECT ActionType from Workflow WHERE ActionName =' + "'" + actionName + "'"
        cursor.execute(sqlQuery)
        for row in cursor:
            return row[0]
    except:
        print("Error while fetching actiontype")


def getEndpoint(db, actionName):
    try:

        cursor = db.cursor()
        sqlQuery = 'SELECT Endpoint from Workflow WHERE ActionName =' + "'" + actionName + "'"
        cursor.execute(sqlQuery)
        for row in cursor:
            return row[0]
    except:
        print("Error while fetching endpoint")


def getResponseCode(db, actionName):
    try:
        cursor = db.cursor()
        sqlQuery = 'SELECT ResponseCode from Workflow WHERE ActionName =' + "'" + actionName + "'"
        cursor.execute(sqlQuery)
        for row in cursor:
            return row[0]

    except:
        print("Error while fetching Response code")


def getEjectHeader(db, actionName):
    try:
        cursor = db.cursor();
        sqlQuery = 'SELECT EjectHeader from Workflow WHERE ActionName =' + "'" + actionName + "'"
        cursor.execute(sqlQuery)
        for row in cursor:
            return row[0]
    except:
        print("Error while fetching EjectHeader")


def getEjectVariable(db, actionName):
    try:
        cursor = db.cursor();
        sqlQuery = 'SELECT EjectVariable from Workflow WHERE ActionName =' + "'" + actionName + "'"
        cursor.execute(sqlQuery)
        for row in cursor:
            return row[0]
    except:
        print("Error while fetching EjectVariable")


def getRequestFileName(db, actionName):
    try:
        cursor = db.cursor();
        sqlQuery = 'SELECT RequestFileName from Workflow WHERE ActionName =' + "'" + actionName + "'"
        cursor.execute(sqlQuery)
        for row in cursor:
            return row[0]
    except:
        print("Error while fetching RequestFileName")


def getResponseFileName(db, actionName):
    try:
        cursor = db.cursor();
        sqlQuery = 'SELECT ResponseFileName from Workflow WHERE ActionName =' + "'" + actionName + "'"
        cursor.execute(sqlQuery)
        for row in cursor:
            return row[0]
    except:
        print("Error while fetching ResponseFileName")


def getHeaderName(db, actionName):
    cursor = db.cursor();
    sqlQuery = 'SELECT HeaderName from Workflow WHERE ActionName =' + "'" + actionName + "'"
    print(sqlQuery)
    cursor.execute(sqlQuery)
    headerName = ''
    for row in cursor:
        headerName = row[0]
    print('HeaderName' + str(headerName))
    sqlQuery = 'SELECT * from Headers WHERE HeaderName =' + "'" + str(headerName) + "'"
    print(sqlQuery)
    headernames = []
    headersvalue = []
    column = cursor.execute(sqlQuery)
    for column in column.description:
        if column[0] != 'index' and column[0] != 'HeaderName':
            headernames.append(column[0])

    for i in headernames:
        sqlQuery = 'SELECT ' + i + ' from Headers WHERE HeaderName =' + "'" + str(headerName) + "'"
        data = cursor.execute(sqlQuery)
        for row in data:
            headersvalue.append(str(row[0]))

    headers = {}
    for j in range(0, len(headersvalue)):
        print(headernames[j])
        print(headersvalue[j])
        headers[headernames[j]] = headersvalue[j]
    return headers


# db = convertExcelIntoDatabase('C:/Users/ragha/Downloads/Projects/RobotFramework/Resources/TestCaseFiles/WorkFlow.xlsx')
# list = getHeaderName(db, 'GetLastName')

# print(list)
