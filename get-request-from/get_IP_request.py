"""
Using a iplify api service to get or know about our ID address
"""

import requests

get_url = 'https://api.ipify.org?format=json'

get_response = requests.get(get_url)
print(get_response.status_code)
# 202


def give_response():
    if (get_response.status_code == 200):
        response = get_response.json()  # <---- give output in json format
        print(response)
    else:
        print(f"Error ;-; {get_response.status_code}")


#defining main function for call upper function

def main():
    result_get = give_response()
    print(result_get)


if __name__ == "__main__":
    main()
