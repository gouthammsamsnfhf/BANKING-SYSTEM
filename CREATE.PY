#installed library mysql-connector-python
import mysql.connector

#creating connection
class insert:
    def __init__(self):

        self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "sanju@98",
                database = "bank"
                )
    def personaldetails(self,cid,fname,lname,addy,ph,an,pan):
        cur = self.connection.cursor() #creating cursor
        #now we can start executing queries
        cur.execute(f"INSERT INTO PERSONALDETAILS VALUES({cid},'{fname}','{lname}','{addy}',{ph},{an},'{pan}')")
        # After inserting data we need to commit changes
        self.connection.commit()
        print("----------personal information has been saved sucessfully----------")
    def bankdetails(self,accn,cid,ifsc,actype):
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO BANKDETAILS VALUES({accn},{cid},'{ifsc}','{actype}')")
        self.connection.commit()
        print("------------Bank details has been saved successfully------------")
    def transactiondetails(self,tid,sac,rac,amt,mthd):
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO TRANSACTIONDETAILS VALUES({tid},{sac},{rac},{amt},'{mthd}')")
        self.connection.commit()
        print("------------Transaction details has been saved successfully------------")
    def accountdetails(self,accn,amt,cbal,tid,trantype):
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO ACCOUNTDETAILS VALUES({accn},{amt},{cbal},{tid},'{trantype}')")
        self.connection.commit()
        print("------------Account details has been saved successfully------------")





