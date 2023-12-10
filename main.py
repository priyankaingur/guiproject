# tkinter comes with python by default
from tkinter import *
import tkinter
# mysql library
import pymysql
# encryption library
from cryptography.fernet import Fernet
import random
# logger module
from logger.log import Logger
from db.insert import load_pii
from db.insert import load_user
from db.insert import load_pfi
from db.insert import load_stocks
from db.insert import load_bonds

# declare logger object and path to store the logs
logger_object = Logger("gui.log")

# declare tkinter objects
window = Tk()
window.title("GUI to Insert data to mysql DB")
window.geometry('400x400')

# declare mysql objects
connect = pymysql.connect(host="localhost", user="root", passwd="root", database="default")
cursor = connect.cursor()

# declare encryption library
key = Fernet.generate_key()
fernet = Fernet(key)

# get binary
# def get_binary():
#     print(newCheckBox)


# define GUI properties
inp = Checkbutton(window, text="checkbox")
# inp = Checkbutton(window, text="checkbox",  onvalue=1, offvalue=0)
input0 = Label(window, text="PII Data").place(x=150, y=30)
input1 = Label(window, text="UserName").place(x=10, y=50)
UserName = Entry(window, show='*')
UserName.place(x=150, y=50)
input2 = Label(window, text="UserEmail").place(x=10, y=70)
UserEmail = Entry(window, show='*')
UserEmail.place(x=150, y=70)
input3 = Label(window, text="UserAddress").place(x=10, y=90)
UserAddress = Entry(window, show='*')
UserAddress.place(x=150, y=90)
inpu42 = Label(window, text="UserContact").place(x=10, y=110)
UserContact = Entry(window, show='*')
UserContact.place(x=150, y=110)
input5 = Label(window, text="UserDoB").place(x=10, y=130)
UserDoB = Entry(window, show='*')
UserDoB.place(x=150, y=130)
input6 = Label(window, text="UserSSN").place(x=10, y=150)
UserSSN = Entry(window, show='*')
UserSSN.place(x=150, y=150)
input7 = Label(window, text="UserDL").place(x=10, y=170)
UserDL = Entry(window, show='*')
UserDL.place(x=150, y=170)
input8 = Label(window, text="PFI Data").place(x=150, y=190)
input9 = Label(window, text="BankAccount").place(x=10, y=210)
BankAccount = Entry(window, show='*')
BankAccount.place(x=150, y=210)
input10 = Label(window, text="RetirementAccount").place(x=10, y=230)
RetirementAccount = Entry(window, show='*')
RetirementAccount.place(x=150, y=230)
input11 = Label(window, text="CCDebt").place(x=10, y=250)
CCDebt = Entry(window, show='*')
CCDebt.place(x=150, y=250)
input12 = Label(window, text="LifeInsurance").place(x=10, y=270)
LifeInsurance = Entry(window, show='*')
LifeInsurance.place(x=150, y=270)
# newCheckBox= IntVar()
# v1 = Checkbutton(window, text='newCheckBok', variable=newCheckBox, onvalue=True, offvalue=False, command=get_binary)
stocks_invested = IntVar()
Checkbutton(window, text="stocks_invested", variable=stocks_invested).place(x=150, y=290)
input13 = Label(window, text="StockName").place(x=10, y=310)
StockName = Entry(window, show='*')
StockName.place(x=150, y=310)
input14 = Label(window, text="StockPurchasePrice").place(x=10, y=330)
StockPurchasePrice = Entry(window, show='*')
StockPurchasePrice.place(x=150, y=330)
input15 = Label(window, text="StockPurchaseQuantity").place(x=10, y=350)
StockPurchaseQuantity = Entry(window, show='*')
StockPurchaseQuantity.place(x=150, y=350)
# print(stocks_invested)
bonds_invested = IntVar()
Checkbutton(window, text="bonds_invested", variable=bonds_invested).place(x=150, y=370)
input13 = Label(window, text="BondName").place(x=10, y=390)
BondName = Entry(window, show='*')
BondName.place(x=150, y=390)
input14 = Label(window, text="BondMaturityDate").place(x=10, y=410)
BondMaturityDate = Entry(window, show='*')
BondMaturityDate.place(x=150, y=410)
input15 = Label(window, text="BondInvestedAmount").place(x=10, y=430)
BondInvestedAmount = Entry(window, show='*')
BondInvestedAmount.place(x=150, y=430)

# function to generate user IDs
def generate_userid():
    try:
        logger_object.info("generated user ID successfully")
        user_id = random.randint(0, 9999999)
        return user_id
    except Exception:
        logger_object.error("unable to generate the user ID")
        return None


# function to insert data into user table
def push_user(uid):
    load = {"uid": uid}
    load_user(**load)


# function to insert data into pii table
def push_pii(uid):
    load = {
        "fernet": fernet,
        "uid": uid,
        "enc_user_name": fernet.encrypt(UserName.get().encode()),
        "enc_user_email": fernet.encrypt(UserEmail.get().encode()),
        "enc_user_address": fernet.encrypt(UserAddress.get().encode()),
        "enc_user_contact": fernet.encrypt(UserContact.get().encode()),
        "enc_user_dob": fernet.encrypt(UserDoB.get().encode()),
        "enc_user_ssn": fernet.encrypt(UserSSN.get().encode()),
        "enc_user_dl": fernet.encrypt(UserDL.get().encode())
    }
    load_pii(**load)


# function to insert data into pfi table
def push_pfi(uid):
    if stocks_invested.get():
        stocks_id = uid,
    else:
        stocks_id = "xxxx"
    if bonds_invested.get():
        bonds_id = uid,
    else:
        bonds_id = "yyyy"
    load = {
        "fernet": fernet,
        "uid": uid,
        "enc_bank_account": fernet.encrypt(BankAccountUserName.get().encode()),
        "enc_retirement_account": fernet.encrypt(RetirementAccount.get().encode()),
        "enc_cc_debt": fernet.encrypt(CCDebt.get().encode()),
        "enc_life_insurance": fernet.encrypt(LifeInsurance.get().encode()),
        "stocks_id": stocks_id,
        "bonds_id": bonds_id
    }
    load_pfi(**load)


def push_stocks_data(uid):
    load = {
    "fernet": fernet,
    "uid": uid,
    "enc_stock_name": fernet.encrypt(StockName.get().encode()),
    "enc_stock_purchase_price": fernet.encrypt(StockPurchasePrice.get().encode()),
    "enc_stock_purchase_quantity": fernet.encrypt(StockPurchaseQuantity.get().encode())
    }
    load_stocks(**load)


def push_bonds_data(uid):
    load = {
        "fernet": fernet,
        "uid": uid,
        "enc_bond_name": fernet.encrypt(BondName.get().encode()),
        "enc_bond_maturity_date": fernet.encrypt(BondMaturityDate.get().encode()),
        "enc_bond_invested_amount": fernet.encrypt(BondInvestedAmount.get().encode())
    }
    load_bonds(**load)

# defining wrapper functon to orchestrate data loading to RDBMS
def push_data():
    uid = generate_userid()
    stocks = stocks_invested.get()
    bonds = bonds_invested.get()
    push_user(uid)
    push_pii(uid)

# push stocks data only if stocks_invested is true
    if stocks:
        # print(stocks_invested.get())
        logger_object.error("pushing stocks invested data for", uid)
        push_stocks_data()
    else:
        logger_object.error("stocks invested was set to false and no data inserted", uid)

# push bonds data only if bonds_invested is true
    if bonds:
        # print(bonds_invested.get())
        logger_object.error("pushing bonds invested data for", uid)
        push_bonds_data()
    else:
        logger_object.error("bonds invested was set to false and no data inserted", uid)


# defining main function
def main():
    pushdata_button = Button(window, text="Push Data", command=push_data)
    pushdata_button.place(x=125, y=460)
    window.mainloop()


if __name__ == "__main__":
    main()
