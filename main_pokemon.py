from api_pokemon import fetch_data
import streamlit as st

# SIDEBAR---------------------------------------------------------------------------------------
with st.sidebar:
    st.title("Projekt Pokemon")
    name = st.text_input("Schreibe den Namen eines Pokemons").lower()
    name = st.selectbox("Oder wähle aus der Liste: ", [""] + ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Raichu"]).lower()
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