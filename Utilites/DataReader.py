import pandas as pd
import sqlite3
import os
def convertExcelIntoDatabase(excelFile):
    try:
      db = sqlite3.connect('sqlite.db')
      dfs = pd.read_excel(excelFile, engine='openpyxl', sheet_name=None)
      for workflow, df in dfs.items():
           df.to_sql(workflow, db,if_exists='replace')
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

def getActionType(db,actionName):

        cursor=db.cursor()
        sqlQuery='SELECT ActionType from Workflow WHERE ActionName ='+"'"+actionName+"'"
        cursor.execute(sqlQuery)
        print("start")
        print(cursor)
        for row in cursor:
            return row[0]



db=convertExcelIntoDatabase('C:/Users/ragha/Downloads/Projects/RobotFramework/Resources/TestCaseFiles/WorkFlow.xlsx')
print(getActionType(db,'GetLastName'))