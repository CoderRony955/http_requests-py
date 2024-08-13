"""
using random api requests for getting dog images """

import requests

my_url = 'https://dog.ceo/api/breeds/image/random'

give_response = requests.get(my_url)
print(give_response.status_code)

print(give_response.status_code)
# 202


def get_response():
    if (give_response.status_code == 200):
        response = give_response.json()
        print(response)

    else:
        print(f"Error ;-; {give_response.status_code}")
        
#defining main function for call upper function

def main():
    result = get_response()
    print(result)


if __name__ == "__main__":
    main()
