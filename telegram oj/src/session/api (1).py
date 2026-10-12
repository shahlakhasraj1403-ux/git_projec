import requests
import app_db

def get_movie_list_by_page(page=1):
    
    url = 'https://moviesapi.ir/api/v1/movies'

    api_params = {'page': page}
    response = requests.get(url, params= api_params)

    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()['data']
        return response
#########################################

def get_genres_list():

    url = 'https://moviesapi.ir/api/v1/genres'

    response = requests.get(url)

    if response.status_code != 200:
        return 'ERROR'
    else:
        return response.json()

#########################################

def get_movies_by_genre(genre_id, page=1):

    url = f'https://moviesapi.ir/api/v1/genres/{genre_id}/movies'

    api_params = {'page': page}
    response = requests.get(url, params=api_params)

    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()['data']
        return response

#########################################

if __name__ == '__main__':
    result = get_movie_list_by_page()
    result2 = app_db.insert_list_of_movies(result)
    print(result2)

