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


def rating_range(min_value, max_value, keyword):
    key = 'eeb4665b'
    url = f"http://www.omdbapi.com/?s={keyword}&apikey={key}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data['Response'] == 'True':
            found_movies = False  
            for movie in data['Search']:
                movie_details_url = f"http://www.omdbapi.com/?i={movie['imdbID']}&apikey={key}"
                details_response = requests.get(movie_details_url)
                details_data = details_response.json()

                if details_data['Response'] == 'True':
                    rating = details_data['imdbRating']
                    if rating is not None: 
                        rating = float(rating)
                        if min_value <= rating <= max_value:
                            print(f"Title: {details_data['Title']}, Rating: {rating}")
                            found_movies = True 

            if not found_movies:
                print("No movies found within that rating range.")

        else:
            print("No movies found.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


while True:
    choice = input("How do you wish to search (via Title or Score)?: ").lower()

    if choice == "title":
        movie_title = input("Enter the movie title: ")
        get_score_title(movie_title)

    elif choice == "score":
        min_value = float(input("Enter the minimum rating: "))
        max_value = float(input("Enter the maximum rating: "))
        keyword = input("Enter a keyword or genre for your search (e.g., 'action', 'comedy'): ")
        rating_range(min_value, max_value, keyword)

    else:
        print("Invalid choice, please try again.")

    keep_running = input("Do you want to run the app again? (Yes/No): ").lower()
    if keep_running != "yes":
        break

            



