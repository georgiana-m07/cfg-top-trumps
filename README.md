# Top Trumps Game - Pokémon vs. Harry Potter

This project is a Python-based terminal game inspired by the classic "Top Trumps" card game. Players can choose between playing with Pokémon or Harry Potter characters, using their stats to compete in rounds to determine the winner.

## Project Overview

In this game, players are dealt a hand of 5 characters (Pokémon or Harry Potter characters) and must choose a stat to compare with their opponent. The game consists of 3 rounds, and the player with the most rounds won is the overall victor.

### Key Features:
- **Choice of Game**: Players can choose to play with either Pokémon or Harry Potter characters.
- **Stat-Based Gameplay**: Players select a stat from their dealt characters to compete against the opponent's characters.
- **API Integration**: The game retrieves live data using two APIs:
  - **Pokémon API**: Fetches stats for randomly selected Pokémon.
  - **Harry Potter API**: Fetches stats for randomly selected Harry Potter characters.
- **Three-Round Format**: The game consists of three rounds, and the player with the highest score at the end is declared the winner.

## How to Play

1. **Game Selection**: Players choose between playing with Pokémon or Harry Potter characters.
2. **Random Hand**: A hand of 5 characters is randomly dealt from the respective universe.
3. **Stat Selection**: For each round, players select a stat to compare against their opponent.
4. **Round Outcome**: The player with the higher stat value wins the round.
5. **Game Conclusion**: After 3 rounds, the game announces the winner based on the number of rounds won.

## Project Structure

- **API URLs**:
  - Pokémon: `https://pokeapi.co/api/v2/pokemon/{}/`
  - Harry Potter: `https://hp-api.onrender.com/api/characters`

- **Main Functions**:
  - `get_pokemon_info(pokemon_number)`: Fetches information about a specific Pokémon using the Pokémon API.
  - `get_harry_potter_characters()`: Fetches a list of Harry Potter characters using the HP API.
  - `random_pokemon_hand()`: Selects 5 random Pokémon from the first 151 Pokémon.
  - `random_harry_potter_hand()`: Selects 5 random Harry Potter characters.
  - `run_pokemon()`: Executes the Pokémon game logic for the player.
  - `run_hp()`: Executes the Harry Potter game logic for the player.
  - `compare_hp_stats()`: Compares the Harry Potter characters' stats based on user selection.

## Requirements

- Python 3.x
- `requests` library for API calls

You can install the required libraries using the following command:
```bash
pip install requests
```

## How to run

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the script in the terminal:
```bash
python top_trumps_game.py
```
4. Follow the instructions in the terminal to choose your game and play.

## Game Flow

1. **Game Start**: The game starts by asking the player to choose between Pokémon and Harry Potter.
2. **Dealing Hands**: The system deals a hand of 5 characters to both the player and the opponent.
3. **Playing Rounds**: Players choose a stat for comparison each round.
4. **Winning Rounds**: A winner is declared after comparing stats for each round.
5. **End of Game**: After 3 rounds, the final scores are displayed, and the winner is announced.


### Example Pokemon Game

1. **Dealt Pokémon**:
  Bulbasaur (Height: 7, Weight: 69, Base Experience: 64)
  Pikachu (Height: 4, Weight: 60, Base Experience: 112)
  ...
2. **Stat Choice**: Choose Height to compete with your opponent's first Pokémon.
3. **Result**: Your Bulbasaur's height is compared with the opponent's Pokémon, and a winner is determined for the round.

### Example Harry Potter Game

1. **Dealt Characters**:
  Harry Potter (Species: human, House: Gryffindor, Alive: True)
  Hermione Granger (Species: human, House: Gryffindor, Alive: True)
  ...
2. **Stat Choice**: Choose House to compete with your opponent's character.
3. **Result**: Your character's house is compared with the opponent’s, and a winner is declared based on the house hierarchy.

## APIs Used

1. **Pokémon API**: The game uses the Pokémon API to retrieve real-time data on Pokémon, including stats like height, weight, and base experience. The Pokémon are selected randomly from the first 151 Pokémon.
  **API URL**: https://pokeapi.co/api/v2/pokemon/{id}/

2. **Harry Potter API**: The Harry Potter API provides information on characters from the Harry Potter universe, including species, house, and whether the character is alive.

  **API URL**: https://hp-api.onrender.com/api/characters

## Future ENhancements

- **Extended Character Pools**: Add more Pokémon and Harry Potter characters beyond the initial pool of 151 Pokémon and the characters available from the HP API.
- **More Stats**: Introduce additional stats for both Pokémon and Harry Potter characters.
- **Multiplayer**: Enable multiplayer functionality where two players can play against each other instead of an AI opponent.
