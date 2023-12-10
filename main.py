# tkinter comes with python by default
from tkinter import *
# mysql library
import pymysql
# encryption library
from cryptography.fernet import Fernet
import random
# logger module
from logger.log import Logger
from db.insert import load_pii
from db.insert import load_user

# declare logger object and path to store the logs
logger_object = Logger("T:\DevTools\Semester-3\COMP-270\guiproject\gui.log")

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

# define GUI properties
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


# defining wrapper functon to orchestrate data loading to RDBMS
def push_data():
    uid = generate_userid()
    push_user(uid)
    push_pii(uid)


# defining main function
def main():
    pushdata_button = Button(window, text="Push Data", command=push_data)
    pushdata_button.place(x=125, y=310)
    window.mainloop()


if __name__ == "__main__":
    main()
