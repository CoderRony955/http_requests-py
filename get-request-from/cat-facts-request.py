"""
using random api requests for getting cat facts """

import requests

my_url = 'https://catfact.ninja/fact'
give_response = requests.get(my_url)

print(give_response.status_code)
# 202


def get_response():
    if (give_response.status_code == 200):
        # in_json = give_response.json()
        # print(in_json)
        print(give_response.content)
    else:
        print(f"Error;-; {give_response.status_code}")


#defining main function for call upper function

def main():
    result = get_response()
    print(result)


if __name__ == "__main__":
    main()
