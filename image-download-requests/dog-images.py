import requests
from PIL import Image
from io import BytesIO

get_url = "https://dog.ceo/api/breeds/image/random"


def get_random_dog_image():
    response = requests.get(get_url)
    print(response.status_code)
    if (response.status_code == 200):
        data = response.json()
        image_url = data['message']
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        img.show()
    else:
        print("Failed to retrieve image")


#defining main function for call upper function

def main():
    give = get_random_dog_image()
    print(give)


if __name__ == "__main__":
    main()

"""PIL (Python Imaging Library): a library for image processing and display.

io: a library for working with input/output streams.

Overall, this program retrieves a random dog image from the Dog CEO API and displays it using Pillow. 
"""
