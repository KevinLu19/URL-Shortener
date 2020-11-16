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
        self.__sql_delete_row = """DELETE FROM url WHERE short_url_key = """

        self.connection = self.__create_connection_database()

        if self.connection is not None:
            self.__create_table(self.connection, self.__sql_create_table)

    def __create_connection_database (self):
        self.__db_connect = None

        try:
            self.__db_connect = sqlite3.connect(self.__db_file_name)
            self.__db_cursor = self.__db_connect.cursor()
            return self.__db_connect

        except sqlite3.Error as e:
            print ("Connection to database failed!")
            print (e)

        return self.__db_connect

    def __create_table (self, db_cursor, sql_command):
        try:
            cursor = db_cursor.cursor()
            cursor.execute(sql_command)

        except sqlite3.Error as e:
            print (e)
            print ("Table already exists!")

    def __clear_table (self):
        db_cursor = self.connection.cursor()

        try:
            db_cursor.execute ("DROP TABLE url")
            print ("Table have been deleted!")

            self.connection.commit()
            self.connection.close()
        except sqlite3.Error as e:
            print (e)

    def set_original_user_url (self, url):
            self.__original_url = url

    def insert_to_table (self, generated_key, original_url):
        sql_key = 1

        db_cursor = self.connection.cursor()

        # self.connection.execute ("INSERT INTO url VALUES ('1','km7NS', 'www.google.com')")
        # self.connection.execute("SELECT * FROM url")
        # print (self.connection.fetchone())

        # self.connection.commit()
        # self.connection.close()

        db_cursor.execute (f"INSERT INTO url VALUES ('{generated_key}','{original_url}')")
        print (f"{generated_key} and {original_url} have been added to the table!")
        self.print_items_from_table()
        # print (db_cursor.fetchone())

        self.connection.commit()
        self.connection.close()

        print (f"Inserted {generated_key} into table")
        sql_key += 1

    def delete_row (self, generated_key):
        complete_sql_command = self.__sql_delete_row + f" {generated_key}"

        db_cursor = self.connection.cursor()
        db_cursor.execute (complete_sql_command)

        self.connection.commit()
        self.connection.close()

    def print_items_from_table (self):
        db_cursor = self.connection.cursor()

        db_cursor.execute("SELECT * FROM url")
        db_cursor.close()

if __name__ == "__main__":
    url_db = URL_DB_Class()
    url_db.insert_to_table("km7NS", str('www.google.com'))

    # sample_url = "https://www.github.com/KevinLu19"
    # short_url = ShortThatURL(sample_url)
    # print(short_url.final_url())