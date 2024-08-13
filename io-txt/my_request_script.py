"""
Using I/O write() function for printing response text in text.txt"""

import requests
import io

my_url = "https://official-joke-api.appspot.com/random_joke"

give_response = requests.get(my_url)
print(give_response.status_code)


def get_response():

    if (give_response.status_code == 200):
        with io.open("print-in-txt-file/text.txt", "w") as file:
            write = file.write(give_response.text)
            print(write)

    else:
        print(f"Error ;-; {give_response.status_code}")


get_response()
