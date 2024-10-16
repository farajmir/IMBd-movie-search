import requests

def get_score_title(title):
    key = 'eeb4665b'
    url = f"http://www.omdbapi.com/?t={title}&apikey={key}"

    try:    
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data['Response'] == 'True':
            print(f"Title: {data['Title']}")
            print(f"IMDb Rating: {data['imdbRating']}")
            print(f"Year: {data['Year']}")
            print(f"Runtime: {data['Runtime']}")
            print(f"Genre(s): {data['Genre']}")
            print(f"Actors: {data['Actors']}")
            print(f"Director: {data['Director']}")
            print(f"Story/Plot: {data['Plot']}")
        else:
            print("Movie not found!")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


while True:
    movie_title = input("Enter the movie title: ")
    get_score_title(movie_title)

    keep_running = input("Do you want to run the app again? (Yes/No): ").lower()
    if keep_running != "yes":
        break
            



