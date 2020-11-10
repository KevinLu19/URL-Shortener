import random
import string
import sqlite3
import os
import sys

db_file_name = "url_storage.db"
db_connect = sqlite3.connect(db_file_name)
# db_cur = db_connect.cursor()

if db_file_name not in os.environ:
    print ("DataBase file not found. Cannot access backend")
    sys.exit(1)

class URL_DB_Class:
    def __init__(self):
        self.db_curr = db_connect.cursor()

    def check_table_exists (self):
        return self.db_curr.execute("CREATE TABLE IF NOT EXIST url()")

    def create_table(self):
        return self.db_curr.execute("CREATE TABLE url(url_parameter, short_url)")

    def insert_to_table(self, item):
        pass

    def comitting_changes(self):
        return self.db_curr.commit()

    def closing_db_connection(self):
        return self.db_curr.close()

if __name__ == "__main__":
    url_db = URL_DB_Class()
