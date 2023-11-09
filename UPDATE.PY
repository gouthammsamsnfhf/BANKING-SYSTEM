import mysql.connector

#creating connection
class update:
    def __init__(self):

        self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "sanju@98",
                database = "bank"
                )
    def myupdate(self,table_name,column_name,new_value,cust_id):
        cur = self.connection.cursor()
        if new_value.isnumeric():
            cur.execute(f"UPDATE {table_name} set {column_name} = {int(new_value)} where customerid = {cust_id}")
        else:
            cur.execute(f"UPDATE {table_name} set {column_name} = '{new_value}' where customerid = {cust_id}")
        self.connection.commit()
        print("successfully updated")
