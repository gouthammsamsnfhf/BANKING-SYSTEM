import mysql.connector

#creating connection
class delete:
    def __init__(self):

        self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "sanju@98",
                database = "bank"
                )
    
    def delete_data(self,table_name,id):
        cur = self.connection.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE CUSTOMERID= {id}")
        self.connection.commit()
        print('------DATA DELETED SUCCESSFULLY------')