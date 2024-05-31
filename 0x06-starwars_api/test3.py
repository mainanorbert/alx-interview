import requests

def get_star_wars_characters(movie_id):
  """
  Fetches characters from a Star Wars movie using the /films/ endpoint.

  Args:
      movie_id: The ID of the Star Wars movie (e.g., 3 for Return of the Jedi).

  Returns:
      A list of character names from the movie.
  """
  url = f"https://swapi.dev/api/films/{movie_id}"
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    characters = data.get("characters")
    if characters:
      for character_url in characters:
        character_response = requests.get(character_url)
        if character_response.status_code == 200:
          character_data = character_response.json()
          print(character_data.get("name"))
    else:
      print("No characters found for this movie.")
  else:
    print(f"Error retrieving movie data: {response.status_code}")

if __name__ == "__main__":
  # Get movie ID from command line argument (assuming script is run as python script.py movie_id)
  import sys
  if len(sys.argv) > 1:
    movie_id = int(sys.argv[1])
    get_star_wars_characters(movie_id)
  else:
    print("Please provide a movie ID as an argument.")

