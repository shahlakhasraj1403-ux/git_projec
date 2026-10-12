import streamlit as st
import api
import app_db
st.title('Streamlit Modern Project')
option = st.sidebar.selectbox('Enter Your Option: ',
('CALL MOVIE LIST BY PAGE', 'INSERT MOVIES FROM API', 'SHOW MOVIES BY GENRE'))

if option == 'CALL MOVIE LIST BY PAGE':
    page_id = st.number_input('Enter Pgae number', min_value=1, max_value=25)
    result = api.get_movie_list_by_page(page_id)
    if st.button('Show Movie List'):
        if result != 'ERROR':
            st.write(result)
        else:
            st.error('Your Request Can Not Be Send!!!')


elif option == 'INSERT MOVIES FROM API':
    page_id = st.number_input('Enter Pgae number', min_value=1, max_value=25)
    result1 = api.get_movie_list_by_page(page_id)
    if st.button('ADD Movie List'):
        if result1 != 'ERROR':
            result2 = app_db.insert_list_of_movies(result1)
            st.success(result2)
            
        else:
            st.error('Your Request Can Not Be Send!!!')


elif option == 'SHOW MOVIES BY GENRE':

    genres_list = api.get_genres_list()

    if genres_list == 'ERROR':
        st.error('Your Request Can Not Be Send!!!')
    else:
        genre_names = [genre['name'] for genre in genres_list]
        selected_genre_name = st.selectbox('Enter Your Genre: ', genre_names)

        selected_genre = next(g for g in genres_list if g['name'] == selected_genre_name)
        genre_id = selected_genre['id']

        page_id = st.number_input('Enter Page number', min_value=1, max_value=25)

        if st.button('Show Movies Of This Genre'):
            result3 = api.get_movies_by_genre(genre_id, page_id)
            if result3 != 'ERROR':
                st.session_state['genre_movies'] = result3
                st.write(result3)
            else:
                st.session_state.pop('genre_movies', None)
                st.error('Your Request Can Not Be Send!!!')

        if st.button('Insert These Movies Into DB'):
            if 'genre_movies' in st.session_state:
                app_db.create_genre_movies_table(app_db.DB_NAME)
                result4 = app_db.insert_list_of_genre_movies(st.session_state['genre_movies'])
                st.success(result4)
            else:
                st.warning('Please Show Movies Of This Genre First!!!')