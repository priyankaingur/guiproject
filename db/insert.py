import pymysql
from logger.log import Logger

# In real-world scenario, the username password is dynamically fetched from secret management system like HasiCorp vault
# including vault is outside scope of this project and for simplicity, dummy connection password is used


# connect = pymysql.connect(host="localhost", user="root", passwd="root", database="default")
# uncomment above for initial run and validation and use below for more secured connection
connect = pymysql.connect(host="localhost", user="root", passwd="root", database="default", ssl_cert="root-cert.pem",
                          ssl_key="root-key.pem", ssl_ca="ca.pem")
cursor = connect.cursor()

# declare logger object
logger_object = Logger("T:\Priyanka\Semester-3\COMP-270 Secure Software Systems\guiproject\gui.log")


# defining constant to re-use in insert statement

# encrypt = "\"', aes_encrypt('\""
# key = " \"','key'), \""
# key_close = "\"' ,'key'))\""


def load_user(**load):
    uid = load['uid']
    try:
        cursor.execute("insert into user(user_id) values('" + str(uid) + "')")
        connect.commit()
        logger_object.info("successfully pushed data to users table")
    except Exception as e:
        logger_object.error("Failed to insert user data")


def load_pii(**load):
    uid = load['uid']
    try:
        fernet = load['fernet']
        enc_user_name = load['enc_user_name']
        enc_user_email = load['enc_user_email']
        enc_user_address = load['enc_user_address']
        enc_user_contact = load['enc_user_contact']
        enc_user_dob = load['enc_user_dob']
        enc_user_ssn = load['enc_user_ssn']
        enc_user_dl = load['enc_user_dl']
        cursor.execute("insert into pii(id, user_name, user_email, address, contact_number, date_of_birth, social_security_number, driver_license)"
            "values('" + str(
                uid) + "', aes_encrypt('" + fernet.decrypt(enc_user_name).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_user_email).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_user_address).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_user_contact).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_user_dob).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_user_ssn).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_user_dl).decode() + "' ,'key'))")
        # defining a constant instead of duplicating literal is not compatible with aws_encryption function; hence
        # ignoring the sonarLint recommendation cursor.execute("insert into pii(id, user_name, user_email, address,
        # contact_number, date_of_birth, social_security_number, driver_license)" "values('" + str( uid) + encrypt +
        # fernet.decrypt(enc_user_name).decode() + key + encrypt + fernet.decrypt(enc_user_email).decode() + key +
        # encrypt + fernet.decrypt(enc_user_address).decode() + key + encrypt + fernet.decrypt(
        # enc_user_contact).decode() + key + encrypt + fernet.decrypt(enc_user_dob).decode() + key + encrypt +
        # fernet.decrypt(enc_user_ssn).decode() + key + encrypt + fernet.decrypt(enc_user_dl).decode() + key_close)
        connect.commit()
        logger_object.info("data has been pushed to pii table " + str(uid))
    except Exception as e:
        print(e)
        logger_object.error("Failed to insert pii data " + str(uid))


def load_pfi(**load):
    uid = load['uid']
    try:
        fernet = load['fernet']
        enc_bank_account = load['enc_bank_account']
        enc_retirement_account = load['enc_retirement_account']
        enc_cc_debt = load['enc_cc_debt']
        enc_life_insurance = load['enc_life_insurance']
        stocks_id = load['stocks_id']
        bonds_id = load['bonds_id']
        cursor.execute(
            "insert into pfi(id, savings_account_number, retirements_account, credit_card_debt, life_insurance, stocks_id, bonds_id)"
            "values('" + str(
                uid) + "', aes_encrypt('" + fernet.decrypt(enc_bank_account).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_retirement_account).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_cc_debt).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_life_insurance).decode() + "','key'), '" + str(stocks_id) + "', '" + str(bonds_id) + "')")
        connect.commit()
        logger_object.info("data has been pushed to pfi table " + str(uid))
    except Exception as e:
        print(e)
        logger_object.info("failed to insert pfi table " + str(uid))


def load_stocks(**load):
    uid = load['uid']
    try:
        fernet = load['fernet']
        enc_stock_name = load['enc_stock_name']
        enc_stock_purchase_price = load['enc_stock_purchase_price']
        enc_stock_purchase_quantity = load['enc_stock_purchase_quantity']
        cursor.execute(
            "insert into stocks_invested(stk_id, stock_name, stock_purchase_price, stock_quantity)"
            "values('" + str(
                uid) + "', aes_encrypt('" + fernet.decrypt(enc_stock_name).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_stock_purchase_price).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_stock_purchase_quantity).decode() + "' ,'key'))")
        connect.commit()
        logger_object.info("data has been pushed to stocks table " + str(uid))
    except Exception as e:
        print(e)
        logger_object.error("failed to insert stocks table " + str(uid))


def load_bonds(**load):
    uid = load['uid']
    try:
        fernet = load['fernet']
        enc_bond_name = load['enc_bond_name']
        enc_bond_maturity_date = load['enc_bond_maturity_date']
        enc_bond_invested_amount = load['enc_bond_invested_amount']
        cursor.execute(
            "insert into bonds_invested(bnd_id, bond_name, maturity_date, invested_amount)"
            "values('" + str(
                uid) + "', aes_encrypt('" + fernet.decrypt(enc_bond_name).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_bond_maturity_date).decode() + "','key'), " + " aes_encrypt('" + fernet.decrypt(enc_bond_invested_amount).decode() + "' ,'key'))")
        connect.commit()
        logger_object.info("data has been pushed to bonds table " + str(uid))
    except Exception as e:
        print(e)
        logger_object.error("failed to insert bonds table " + str(uid))
