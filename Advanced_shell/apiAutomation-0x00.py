import requests

pocketbase_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon_name):
    """
    Fetches data for a given Pokémon from the PokéAPI.
    
    Args:
        pokemon_name (str): The name of the Pokémon to fetch data for.
        
    Returns:
        dict: The JSON response containing Pokémon data.
    """
    try:
        response = requests.get(f"{pocketbase_url}{pokemon_name.lower()}")
        response.raise_for_status()  # Raise an error for bad responses
        with open('data.json', 'w') as file:
            file.write(response.text)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {pokemon_name}: {e}")
        return None
    
def main():
    pokemon_name = input("Enter the name of the Pokémon: ")
    data = get_pokemon_data(pokemon_name)
    
    if data:
        print(f"Data for {pokemon_name.capitalize()}:")
        print(data)
    else:
        print("Failed to retrieve data.")
if __name__ == "__main__":
    main()
