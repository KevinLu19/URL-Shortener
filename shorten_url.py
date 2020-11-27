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
        self.uri_key = ""

    def generate_url_key(self):
        char = string.ascii_letters
        # joined_url_key_string = ''.join(random.choice(char) for _ in range(7))
        joined_url_key_string = ""

        for letters in range (7):
            joined_url_key_string += random.choice(char)

        self.uri_key += joined_url_key_string

        return joined_url_key_string

    def final_url(self):
        # new_url = ""
        # new_url += self.generate_url_key()

        final_destination_url = "https://www.shortthaturl.com/" + self.uri_key
        return final_destination_url
class URL_DB_Class:
    def __init__(self):
        # self.__db_curr = db_connect.cursor()
        self.__db_file_name = "url_storage.db"
        self._original_url = ""
        self.__sql_create_table = """CREATE TABLE IF NOT EXISTS url (
                                        short_url_key text,
                                        original_url text
                                        );"""

        self.__sql_delete_row = """DELETE FROM url WHERE short_url_key = """

        self.__db_connect = sqlite3.connect(self.__db_file_name)
        self.__db_cursor = self.__db_connect.cursor()
        self.__create_table (self.__db_cursor, self.__sql_create_table)
        self._one_url_list = []

    def __del__(self):
        self.__db_connect.close()

    def __create_table (self, db_cursor, sql_command):
        try:
            self.__db_cursor.execute(sql_command)
            print ("------------")
            print ("Table successfully created!")
            print ("------------")

        except sqlite3.Error as e:
            print (e)
            print ("Table already exists!")

    def __clear_table (self):
        try:
            self.__db_cursor.execute ("DROP TABLE url")
            print ("------------")
            print ("Table have been deleted!")
            print ("------------")

            self.__db_connect.commit()
            self.__db_connect.close()
        except sqlite3.Error as e:
            print (e)

    def set_original_user_url (self, url):
        self._original_url = url

    def check_original_url (self):
        if self._original_url is not None:
            pass
        else:
            print ("Your entered url is invalid.")

    def print_original_url (self):
        print (f"The original url is: {self._original_url}")

    def url_to_list (self):
        short_url_class = ShortThatURL(self._original_url)
        url_key = short_url_class.generate_url_key()
        complete_url = short_url_class.final_url()

        # self._one_url_list.append(url_key, self._original_url, complete_url)
        self._one_url_list.extend((url_key, self._original_url, complete_url))

        self.insert_to_table()

    def get_complete_url (self, original_url):
        # self._sql_return_column = f"SELECT short_url_key from url WHERE original_url LIKE '{original_url}' ;"
        # return_key_from_db = self.__db_cursor.execute (self._sql_return_column)
        # print (f"Successfully found {original_url} from table.")

        # self.__db_connect.commit()
        # self.__db_connect.close()

        # complete_uri_link = "https://www.shortthaturl.com/" + str(return_key_from_db)

        complete_uri_link = self._one_url_list[2]
        complete_url = "https://www.shortthaturl.com/" + complete_uri_link

        return complete_url

    def insert_to_table (self):
        generated_key = self._one_url_list[0]
        original_key = self._one_url_list[1]
        completed_url = self._one_url_list[2]

        self.__db_cursor.execute (f"INSERT INTO url VALUES ('{generated_key}', '{original_key}')")
        print (f"{generated_key} and {original_key} have been added to the table! The final url is {completed_url}")

        self.__db_connect.commit()
        self.__db_connect.close()

    def delete_row (self, generated_key):
        complete_sql_command = self.__sql_delete_row + f" {generated_key}"

        db_cursor = self.connection.cursor()
        db_cursor.execute (complete_sql_command)

        self.connection.commit()
        self.connection.close()

if __name__ == "__main__":
    url_db = URL_DB_Class()
    # url_db.clear_table()
    url_db.get_complete_url("www.google.com")
    # url_db.insert_to_table("km7NS", 'www.google.com')

    # sample_url = "https://www.github.com/KevinLu19"
    # short_url = ShortThatURL(sample_url)
    # print(short_url.final_url())