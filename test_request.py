"""
Using request module(library) for taking requests from HTTP in this directory becuase requests module in Python is a powerful library used for making HTTP requests. It simplifies the process of interacting with web services and APIs.
"""

import requests
# create a url variable and put the api link in this
# <----- in this program using api of appspot for taking random jokes
my_url = "https://official-joke-api.appspot.com/random_joke"


def get_response():

    give_response = requests.get(my_url)
    # <---- checking this status of response using status_Code statement if it comes 200 then it's is get successful response if it's come 404 then it's unsuccessful fir get HTTP request
    print(give_response.status_code)

    # 202

    # condtion
    if (give_response.status_code == 200):
        print(give_response.text)  # <--- print joke
    else:
        print(f"Error ;-; {give_response.status_code}")


#defining main function for call upper function

def main():
    result = get_response()
    print(result)


if __name__ == "__main__":

    main()
