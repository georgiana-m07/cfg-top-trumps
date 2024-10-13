import random
import requests

# API URLs
url_pokemon = 'https://pokeapi.co/api/v2/pokemon/{}/'
url_hp = 'https://hp-api.onrender.com/api/characters'

# Welcome message and rules
print("Welcome to Top Trumps game.\n")
game = input("Please choose which game you would like to play (Pokemon or Harry Potter): ").lower()

if game == "pokemon":
    print("You chose the Pokemon game.\n"
          "In this game, you will be dealt a hand of 5 Pokemon.\n"
          "Choose to play a stat to beat your opponent.\n"
          "There are going to be 3 rounds in the game, the player with the highest number of rounds won wins the game.\n"
          "Good luck!")
elif game == "harry potter":
    print("You chose the Harry Potter game.\n"
          "In this game, you will be dealt a hand of 5 Harry Potter Characters.\n"
          "Choose to play a stat to beat your opponent.\n"
          "There are going to be 3 rounds in the game, the player with the highest number of rounds won wins the game.\n"
          "Good luck!")
else:
    print("Invalid game choice. Please run the program again and choose either Pokemon or Harry Potter.")
    exit()


# Function to get pokemon from the API
def get_pokemon_info(pokemon_number):
    url = url_pokemon.format(pokemon_number)
    response = requests.get(url)
    if response.status_code == 200:
        pokemon = response.json()
        return {
            'name': pokemon['name'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'base_experience': pokemon['base_experience']
        }
    else:
        print(f"Failed to retrieve Pokemon with number {pokemon_number}")
        return None


# Function to get 5 random cards of pokemon out of the 151 available
def random_pokemon_hand():
    pokemon_numbers = random.sample(range(1, 151), 5)
    pokemon_hand = []
    for number in pokemon_numbers:
        pokemon_info = get_pokemon_info(number)
        if pokemon_info:
            pokemon_hand.append(pokemon_info)
    return pokemon_hand


# Print the hand of pokemon with their stats
def print_pokemon_hand(pokemon_hand):
    print("You were dealt the following Pokémon:")
    for i, pokemon in enumerate(pokemon_hand, start=1):
        print(
            f"{i}. {pokemon['name'].capitalize()} (Height: {pokemon['height']}, Weight: {pokemon['weight']}, Base Experience: {pokemon['base_experience']})")


# Function to get hp characters from the API
def get_harry_potter_characters():
    response = requests.get(url_hp)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve characters")
        return None


# Function to get 5 random harry potter characters
def random_harry_potter_hand():
    characters = get_harry_potter_characters()
    if not characters:
        return []
    random_characters = random.sample(characters, min(5, len(characters)))
    hp_hand = []
    for character in random_characters:
        hp_hand.append({
            'name': character['name'],
            'species': character['species'],
            'house': character['house'],
            'alive': character['alive']
        })
    return hp_hand


# Print the hand of hp characters with their stats
def print_hp_hand(hp_hand):
    print("You were dealt the following Harry Potter characters:")
    for i, character in enumerate(hp_hand, start=1):
        print(
            f"{i}. {character['name']} (Species: {character['species']}, House: {character['house']}, Alive: {character['alive']}")


# Function to run the pokemon game
def run_pokemon(my_pokemon_hand):
    print_pokemon_hand(my_pokemon_hand)

    if my_pokemon_hand:
        pokemon_choice = int(input('Choose the Pokemon you want to play by selecting number 1-5: ')) - 1
        if pokemon_choice < 0 or pokemon_choice >= len(my_pokemon_hand):
            print('This choice is not valid!')
            return None, None

        my_pokemon = my_pokemon_hand[pokemon_choice]
        print(f'You chose {my_pokemon["name"].capitalize()}')

        stat_choice = input(
            'Which Pokémon stat do you want to use? (height, weight, base_experience): ').strip().lower()

        if stat_choice not in ['height', 'weight', 'base_experience']:
            print("Invalid stat choice!")
            return None, None
        opponent_pokemon_hand = random_pokemon_hand()

        if opponent_pokemon_hand:
            opponent_pokemon = opponent_pokemon_hand[0]
            print(f'The opponent chose {opponent_pokemon["name"].capitalize()}')
            print(
                f'The opponent\'s stats were: name: {opponent_pokemon["name"].capitalize()}, height: {opponent_pokemon["height"]}, weight: {opponent_pokemon["weight"]}, base experience: {opponent_pokemon["base_experience"]}')
            my_stat = my_pokemon[stat_choice]
            opponent_stat = opponent_pokemon[stat_choice]
            return my_stat, opponent_stat

    print("Failed to retrieve your Pokémon. Try again!")

    return None, None


# Function to run the harry potter game
def run_hp(my_hp_hand):
    print_hp_hand(my_hp_hand)

    if my_hp_hand:
        character_choice = int(input('Choose the character you want to play by selecting number 1-5: ')) - 1

        if character_choice < 0 or character_choice >= len(my_hp_hand):
            print('This choice is not valid!')
            return None, None, None

        my_character = my_hp_hand[character_choice]
        print(f'You chose {my_character["name"]}')
        stat_choice = input('Which stat do you want to use? (species, house, alive): ').strip().lower()

        if stat_choice not in ['species', 'house', 'alive']:
            print("Invalid stat choice!")
            return None, None, None
        opponent_hp_hand = random_harry_potter_hand()

        if opponent_hp_hand:
            opponent_character = opponent_hp_hand[0]
            print(f'The opponent chose {opponent_character["name"]}')
            print(
                f'The opponent\'s stats were: name: {opponent_character["name"]}, species: {opponent_character["species"]}, house: {opponent_character["house"]}, alive: {opponent_character["alive"]}')
            my_stat = my_character[stat_choice]
            opponent_stat = opponent_character[stat_choice]
            return my_stat, opponent_stat, stat_choice

    print("Failed to retrieve your character. Try again!")

    return None, None, None


# Function to compare Harry Potter stats
def compare_hp_stats(my_stat, opponent_stat, stat_choice):
    if stat_choice == 'species':
        return (my_stat == 'human') > (opponent_stat == 'human')

    elif stat_choice == 'house':
        house_order = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
        if my_stat in house_order and opponent_stat in house_order:
            return house_order.index(my_stat) < house_order.index(opponent_stat)
        return my_stat in house_order and opponent_stat not in house_order

    elif stat_choice == 'alive':
        return my_stat and not opponent_stat

    return False


# Main game loop
max_rounds = 3
player_score = 0
opponent_score = 0

for round_counter in range(1, max_rounds + 1):
    print(f"\nRound number {round_counter}")

    if game == "pokemon":
        player_hand = random_pokemon_hand()
        my_stat, opponent_stat = run_pokemon(player_hand)
        if my_stat is not None and opponent_stat is not None:
            if my_stat > opponent_stat:
                player_score += 1
                print('You win this round!')
            elif my_stat < opponent_stat:
                opponent_score += 1
                print('You lose this round!')
            else:
                print('This round is a draw!')

    elif game == "harry potter":
        player_hand = random_harry_potter_hand()
        my_stat, opponent_stat, stat_choice = run_hp(player_hand)

        if my_stat is not None and opponent_stat is not None and stat_choice is not None:
            print(f"Your {stat_choice}: {my_stat}")
            print(f"Opponent's {stat_choice}: {opponent_stat}")
            if compare_hp_stats(my_stat, opponent_stat, stat_choice):
                player_score += 1
                print('You win this round!')
            else:
                opponent_score += 1
                print('You lose this round!')
        else:
            print("An error occurred. Skipping this round.")

# End the game by showing the overall winner
print(f"\nGame over! You've played {max_rounds} rounds.")
print(f"Final scores:\nPlayer: {player_score}\nOpponent: {opponent_score}")

if player_score > opponent_score:
    print("Congratulations! You've won the game!")
elif player_score < opponent_score:
    print("The opponent won the game. Better luck next time!")
else:
    print("It's a draw! Start another game.")