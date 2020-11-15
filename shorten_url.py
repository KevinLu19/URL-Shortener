import random
import string
import sqlite3
import requests
import sys

from urllib.request import pathname2url

# db_file_name = "url_storage.db"

# try:
#     db_uri = f"file:{pathname2url(db_file_name)}?mode=rw"
#     db_connect = sqlite3.connect(db_uri, uri=True)

# except sqlite3.OperationalError:
#     print ("DataBase file not found. Cannot access backend file. Please check error.")
#     sys.exit(1)

class ShortThatURL():
    def __init__(self, long_url):
        self.original_url = long_url

    def generate_url_key(self):
        char = string.ascii_letters
        # joined_url_key_string = ''.join(random.choice(char) for _ in range(7))
        joined_url_key_string = ""

        for letters in range (7):
            joined_url_key_string += random.choice(char)

        return joined_url_key_string

    def final_url(self):
        new_url = ""
        new_url += self.generate_url_key()

        final_destination_url = "https://www.shortthaturl.com/" + new_url
        return final_destination_url

class URL_DB_Class:
    def __init__(self):
        # self.__db_curr = db_connect.cursor()
        self.__db_file_name = "url_storage.db"
        self.__original_url = ""
        self.__sql_create_table = """CREATE TABLE IF NOT EXISTS url (
                                        short_url_key text,
                                        original_url text);"""

        self.connection = self.__create_connection_database()

        if self.connection is not None:
            self.__create_table(self.connection, self.__sql_create_table)

        # try:
        #     self.db_conn = sqlite3.connect(self.__db_file_name)
        #     print ("Connected to DataBase")
        # except sqlite3.Error as e:
        #     print (e)
        # finally:
        #     if self.db_conn:
        #         self.db_conn.close()

        # if self.db_conn is not None:
        #     self.__create_table (self.__sql_create_table)
        # else:
        #     print ("Cannot create table in database!")

    def __create_connection_database (self):
        self.__db_connect = None

        try:
            self.__db_connect = sqlite3.connect(self.__db_file_name)
            self.__db_cursor = self.__db_connect.cursor()
            return self.__db_connect

        except sqlite3.Error as e:
            print ("Connection to database failed!")
            print (e)

        # self.__create_table(self.__sql_create_table)
        # if self.__db_connect is not None:
        #     self.__create_table (self.__sql_create_table)

        return self.__db_connect

    def __create_table (self, db_cursor, sql_command):
        # connection = self.__create_connection_database()

        # if connection is not None:
        #     # self.__db_cursor = self.__db_connect.cursor()
        #     self.__db_cursor.execute(sql_command)

        try:
            cursor = db_cursor.cursor()
            cursor.execute(sql_command)

        except sqlite3.Error as e:
            print (e)

        # try:
        #     self.__db_curr.execute(sql_command)
        # except sqlite3.Error as e:
        #     print ("Table already exists!")
        #     print (e)
        #     sys.exit(1)

    def set_original_user_url (self, url):
            self.__original_url = url

    def insert_to_table (self, generated_key, original_url):
        sql_key = 1

        # sql_insert_command = "INSERT INTO url (id, short_url_key, original_url) VALUES(?,?,?)"

        #self.connection.execute(f"INSERT INTO url VALUES ({sql_key}, {generated_key}, {original_url})")
        self.connection.execute(f"INSERT INTO url (short_url_key, original_url) VALUES({generated_key},{original_url})")

        self.connection.commit()
        self.connection.close()

        print (f"Inserted {generated_key} into table")
        sql_key += 1

    def print_items_from_table (self):
        self.__db_cursor.execute("SELECT * FROM url")

if __name__ == "__main__":
    url_db = URL_DB_Class()
    url_db.insert_to_table("km7NS", str('www.google.com'))
    url_db.comitting_changes()

    # sample_url = "https://www.github.com/KevinLu19"
    # short_url = ShortThatURL(sample_url)
    # print(short_url.final_url())