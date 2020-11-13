import random
import string
import sqlite3
import requests
import sys

from urllib.request import pathname2url

db_file_name = "url_storage.db"

try:
    db_uri = f"file:{pathname2url(db_file_name)}?mode=rw"
    db_connect = sqlite3.connect(db_uri, uri=True)

except sqlite3.OperationalError:
    print ("DataBase file not found. Cannot access backend file. Please check error.")
    sys.exit(1)

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
        # return final_destination_url

        return final_destination_url

class URL_DB_Class:
    def __init__(self):
        self.db_curr = db_connect.cursor()

    def create_table(self):
        try:
            self.db_curr.execute("CREATE TABLE url()")
        except:
            print ("Table already exists!")
            sys.exit(1)

    def insert_to_table(self, item):
        self.db_curr.execute(f"INSERT INTO url({item})")

    def comitting_changes(self):
        return self.db_curr.commit()

    def closing_db_connection(self):
        return self.db_curr.close()

if __name__ == "__main__":
    url_db = URL_DB_Class()
    sample_url = "https://www.github.com/KevinLu19"
    short_url = ShortThatURL(sample_url)
    print(short_url.final_url())