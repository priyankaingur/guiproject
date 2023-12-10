# guiproject

## Intro

code base to generate a GUI to accept sensitive data and insert to a database

## Prerequisite

- pip install -r requirements.txt
- MySQL running in local
- update DB connection parameters under db/insert.py

## Description

1. ensure prerequisite are completed
2. executing main.py will generate a gui
3. watch the IDE terminal to troubleshoot any DB connectivity errors
4. connect to the database to ensure data gets inserted as expected

## Logger module

1. created a secured logger module
2. helps to generate and organize logs with different priority
3. customize logs path based on the project need
4. explore logger/log.py to get more insights into the logger module
5. refer gui.log for the logging format and it is highly customizable per project need

## insert module

1. insert module connects to database securly
2. input data is secured by cryptography library
3. data at rest is secured by in-built encryption algorithm
4. data extraction should include correct decryption algorithm to view the data
5. In real-world scenario, the connection parameters like username, password, db hostname is dynamically fetched from secret management system like HasiCorp vault
6. including vault is outside scope of this project and for simplicity, dummy connection password is used