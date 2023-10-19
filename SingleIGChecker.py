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
            return f"Username '{username}' is available on Instagram."
        else:
            return f"Username '{username}' is not available on  Instagram."
    else:
        return "Error connecting to Instagram."
    
if __name__ == "__main__":
    username = input("Enter the username you want to check: ")
    result = check_instagram_username(username)
    print(result)
