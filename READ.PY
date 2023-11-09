import mysql.connector

#creating connection
class read:
    def __init__(self):

        self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "sanju@98",
                database = "bank"
                )
    def specific_info(self,cus_id,table_name):
        cur = self.connection.cursor()
        if table_name == "personaldetails" or table_name == "bankdetails":
            cur.execute(f"SELECT * FROM {table_name} WHERE CUSTOMERID = {cus_id}")
            print(cur.fetchall()) #to display all data we use fetchall function

        #based on cus id we need to fetch transaction details
        if table_name == "transactiondetails":
            cur.execute(f''' SELECT * FROM TRANSACTIONDETAILS WHERE TRANSACTIONID IN
                (SELECT TRANSACTIONID FROM ACCOUNTDETAILS WHERE ACCOUNT_NUMBER IN
                (SELECT ACCOUNT_NUMBER FROM BANKDETAILS WHERE CUSTOMERID = {cus_id})) ''')
            print(cur.fetchall())