"""
Using a zenqoute http api requests to get random qoute
s"""

import requests

get_url = 'https://zenquotes.io/api/random'
give_response = requests.get(get_url)

print(give_response.status_code)
# 202


def get_response():
    if (give_response.status_code == 200):
        response = give_response.json()
        print(response)
    else:
        print(f"Error ;-;, {give_response.status_code}")


def main():
    result = get_response()
    print(result)


if __name__ == "__main__":
    main()
