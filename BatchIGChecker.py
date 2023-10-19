import requests
from bs4 import BeautifulSoup
import time

def check_instagram_username(username):
    base_url = f"https://www.instagram.com/{username}/"
    response = requests.get(base_url)
    username = username.lower()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if username not in soup.get_text():
            return f"Username '{username}' is available on  Instagram."
        else:
            return f"Username '{username}' is not available on  Instagram."
    else:
        return "Error connecting to Instagram."
    
def main():
    with open('usernames.txt', 'r') as file:
        usernames = file.read().splitlines()

    results = []

    for username in usernames:
        result = check_instagram_username(username)
        results.append(result)

    with open('output.txt', 'w') as output_file:
        for result in results:
            output_file.write(result + '\n')

if __name__ == "__main__":
    main()
