import pymysql
from logger.log import Logger

# In real-world scenario, the username password is dynamically fetched from secret management system like HasiCorp vault
# including vault is outside scope of this project and for simplicity, dummy connection password is used


connect = pymysql.connect(host="localhost", user="root", passwd="root", database="default")
# uncomment above for initial run and validation and use below for more secured connection
# connect = pymysql.connect(host="localhost", user="root", passwd="root", database="default", ssl_cert="root-cert.pem",
#                           ssl_key="root-key.pem", ssl_ca="ca.pem")
cursor = connect.cursor()

# from cryptography.fernet import Fernet

logger_object = Logger("T:\DevTools\Semester-2\COMP-261\guiproject\gui.log")


def load_user(**load):
    uid = load['uid']
    try:
        cursor.execute("insert into user(user_id) values('" + str(uid) + "')")
        connect.commit()
        logger_object.info("successfully pushed data to users table")
    except Exception as e:
        logger_object.error("Failed to insert user data")


def load_pii(**load):
    try:
        fernet = load['fernet']
        uid = load['uid']
        enc_user_name = load['enc_user_name']
        enc_user_email = load['enc_user_email']
        enc_user_address = load['enc_user_address']
        enc_user_contact = load['enc_user_contact']
        enc_user_dob = load['enc_user_dob']
        enc_user_ssn = load['enc_user_ssn']
        enc_user_dl = load['enc_user_dl']
        cursor.execute(
            "insert into pii(id, user_name, user_email, address, contact_number, date_of_birth, "
            "social_security_number, driver_license)"
            "values('" + str(
                uid) + "', aes_encrypt(('" + fernet.decrypt(enc_user_name).decode() + "'),'key'), '" + fernet.decrypt(
                enc_user_email).decode() + "', '" + fernet.decrypt(
                enc_user_address).decode() + "','" + fernet.decrypt(enc_user_contact).decode() + "','" + fernet.decrypt(
                enc_user_dob).decode() + "','" + fernet.decrypt(enc_user_ssn).decode() + "','" + fernet.decrypt(
                enc_user_dl).decode() + "')")
        connect.commit()
        logger_object.info("data has been pushed to pii table")
    except Exception as e:
        print(e)
        logger_object.error("Failed to insert pii data")
        return None
