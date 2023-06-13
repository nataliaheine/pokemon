import requests
from bs4 import BeautifulSoup
import streamlit as st

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

# SIDEBAR---------------------------------------------------------------------------------------
with st.sidebar:
    st.title("Projekt Pokemon")
    name_input = st.text_input("Schreibe den Namen eines Pokemons").lower()
    name_select = st.selectbox("Oder wähle aus der Liste: ", [""] + ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Raichu"]).lower()
    
    if name_select and not name_input:
        name = name_select
    else:
        name = name_input
        
    st.info("Die Liste ist klein. Mir war einfach nur wichtig, dass es funktioniert.")
    st.info("Man kann aber selber jeden beliebigen Namen eingeben")
    st.info("Oder versuche einen ungültigen Namen zu schreiben")
    st.info("Woher die Bilder von Pokemons sind, kann man in api_pokemon.py sehen")
    #st.title("Einige Pokemonnamen, die du ausprobieren kannst:")
    # Nur so konnte ich die Namen untereinander geschrieben kriegen:
    #pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Raichu"]
    #for pokemon in pokemons:
    #    st.text(pokemon)

# MAINFRAME-------------------------------------------------------------------------------------
if name != "": # Sonst sieht man einen Fehler bis man einen Namen eingegeben hat
    if fetch_data(name) == False: 
        st.info(f"Es gibt kein Pokemon mit dem Namen {name}. Versuche es nochmal!")
    elif fetch_data(name):
        data, link_img = fetch_data(name)
        pokemon_name = data["name"]
        height = data["height"]
        weight = data["weight"]

        st.title(name.upper())
        st.image(link_img, width=30)

        st.header("Infos:")
        st.write(f"Größe: {height}")
        st.write(f"Gewicht: {weight}")

        abilities = []
        for ability in data["abilities"]:
            abilities.append(ability["ability"]["name"])

        string = ", ".join(abilities)

        st.write(f"Fächigkeiten: {string}")

        types = []
        for typee in data["types"]:
            types.append(typee["type"]["name"])

        string = ", ".join(types)

        st.write(f"Typ: {string}")
