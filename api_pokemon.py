import requests
from bs4 import BeautifulSoup

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_data(name):

    # Daten von pokeapi.co
    FULL_URL = BASE_URL+name
    responce = requests.get(FULL_URL)
    if responce.status_code == 404:    #Falls der Name bei pokeapi nicht gefunden wurde
        return False 
    else:
        data = responce.json()


    # pokeapi hat keine Bilder
    # aber eine andere Webseite hat eine Liste mit allen Pokemons und ihre Bilder
    # Hier wird der Link zum Bild des Pokemons erworben
    responce_img = requests.get("https://www.pokewiki.de/Pok%C3%A9mon-Liste")
    soup = BeautifulSoup(responce_img.text, "html.parser")

    index = data["id"]
    for i in range(1):
        img = soup.find_all("img")[index-1]
        link = img["src"]
        link_img = "https://www.pokewiki.de" + link

    return data, link_img

