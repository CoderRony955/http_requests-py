import requests

BASE_URL = 'https://api.open-meteo.com/v1/forecast'

params = {
    'latitude': 28.6139,  # Latitude for Delhi
    'longitude': 77.2090,  # Longitude for Delhi
    'hourly': 'temperature_2m',  # Example parameter to get hourly temperature
}

# Define the complete URL for weather data
url = f'{BASE_URL}'

# GET Request: Get current weather data


def get_weather():
    response = requests.get(url, params=params)
    print('GET Request:')
    print(f'Status Code: {response.status_code}')
    print(f'Response Content: {response.json()}')

# POST Request: For demonstration purposes, this will send data to a test API


def post_data():
    test_url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post(test_url, json=data)
    print('POST Request:')
    print(f'Status Code: {response.status_code}')
    print(f'Response Content: {response.json()}')

# HEAD Request: Get headers for the weather data


def head_request():
    response = requests.head(url, params=params)
    print('HEAD Request:')
    print(f'Status Code: {response.status_code}')
    print(f'Response Headers: {response.headers}')


#defining main function for call upper functions

def main():
    get_weather()
    post_data()
    head_request()


if __name__ == "__main__":
    main()
