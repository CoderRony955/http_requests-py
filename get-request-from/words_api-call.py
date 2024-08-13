import requests


def get_definition(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            data = response.json()
            definitions = []
            for meaning in data[0]['meanings']:
                for definition in meaning['definitions']:
                    definitions.append(definition['definition'])
            return {'word': word, 'definitions': definitions}
        else:
            return {"error": f"Error {response.status_code}: {response.reason}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred: {e}"}

#defining main function for call upper function

def main():
    word = input("Enter the word: ")
    result = get_definition(word)
    print(result)


if __name__ == "__main__":
    main()
