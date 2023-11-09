from CREATE import insert
from READ import read
from UPDATE import update
from DELETE import delete

obj = insert()
obj1 = read()
obj2 = update()
obj3 = delete()

print("------------Bank Management System------------")
print("For inserting the data press 1: ")
print("For Reading the data press 2: ")
print("For Updating the data press 3: ")
print("For Deleting the data press 4: ")

opr = int(input("Please enter your operation"))

def myopr():
    print("------For Personal information press 1 ------")
    print("------For Bank details press 2 ------")
    print("------For Transaction details press 3 ------")
    print("------For Account details press 4 ------")
    vr = int(input("Please select your table: "))
    if vr ==1:
        return 'personaldetails'
    elif vr == 2:
        return 'bankdetails'
    elif vr == 3:
        return 'transactiondetails'
    elif vr == 4:
        return 'accountdetails'
    
if opr == 1: #user want to insert data if user selects opr as 1
    h = myopr()
    if h == 'personaldetails':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addy = input("please enter address:")
        ph = int(input("please enter phone number:"))
        an = int(input("please enter aadhar number:"))
        pan = input("please enter pan number:")

        obj.personaldetails(cid,fname,lname,addy,ph,an,pan)

    elif h == 'bankdetails':
        acn = int(input("please enter account number:"))
        cid = int(input("please enter customer id:"))
        ifsc = input("please enter IFSC code:")
        actype = input("please enter account type:")

        obj.bankdetails(acn,cid,ifsc,actype)

    elif h == 'transactiondetails':
        tid = int(input("please enter transaction id:"))
        sac = int(input("please enter sender account:"))
        rac = int(input("please enter receiver account:"))
        amt = int(input("please enter amount:"))
        mthd = input("please enter method type:")

        obj.transactiondetails(tid,sac,rac,amt,mthd)
    
    elif h == 'accountdetails':
        accn = int(input("please enter account number:"))
        amt = int(input("please enter amount:"))
        cbal = int(input("please enter closing balance:"))
        tid = int(input("please enter transaction id:"))
        trantype = input("please enter transaction type:")

        obj.accountdetails(accn,amt,cbal,tid,trantype)

if opr == 2: #user want to read data if user selects opr as 2 
    i = myopr()
    cusid = int(input("please enter customer id for fetching data:"))
    obj1.specific_info(cusid,i)
    
if opr == 3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data:"))
    colname = input("please enter column name")
    newval = input("please enter new value")
    obj2.myupdate(j,colname,newval,cusid)

if opr == 4:
    k = myopr() 
    cid = int(input("please enter Customer id to delete data from table"))
    obj3.delete_data(k,cid)