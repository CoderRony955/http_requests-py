"""
taking input from the user, when the user enter the http url then as per url user get response"""
import requests

# <--- taking input from the user. Enter the request url here
my_url = input("Enter the url here to get response: ")

give_response = requests.get(my_url)
print(give_response.status_code)


def get_response():
    if (give_response.status_code == 200):
        print("here is joke for you :)")
        print(give_response.text)
    else:
        print(f"Error ;-; {give_response.status_code}")


#defining main function for call upper function

def main():
    get_result = get_response()
    print(get_result)
    
if __name__ == "__main__":
    main()