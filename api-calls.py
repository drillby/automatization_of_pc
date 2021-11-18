import requests
import json


def main():
    api_url = "http://randomfox.ca/floof"
    response = requests.get(api_url)

    print(response.status_code)

    print(response.text)

    print(response.json())

    fox = response.json()

    print(fox["image"])
    print(fox["link"])


if __name__ == "__main__":
    main()
