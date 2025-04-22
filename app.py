# import pandas as pd
# import streamlit as st
# import pickle
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies =[]
#     for i in movies_list:
#         movie_id =i[0]
#         # fetch poster from api
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
#
# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similar.pkl','rb'))
# st.title('Movie Recommender System')
# selected_movie_name = st.selectbox(
# 'How would you like to be contacted?',
# movies['title'].values)
#
# if st.button('Recommend'):
#     recommentations = recommend(selected_movie_name)
#     for i in recommentations:
#         st.write(i)
#


#
# import streamlit as st
# import pandas as pd
# import requests
# import pickle
#
#
# # Function to fetch movie details (Poster, Title, Overview)
# def fetch_movie_details(movie_name):
#     try:
#         # Search for the movie in TMDb
#         search_url = f"https://api.themoviedb.org/3/search/movie?api_key=YOUR_TMDB_API_KEY&query={movie_name}"
#         response = requests.get(search_url)
#         data = response.json()
#
#         # Check if results exist
#         if data['results']:
#             movie = data['results'][0]  # Get first search result
#             title = movie.get('title', 'Unknown')
#             overview = movie.get('overview', 'No description available.')
#             poster_url = "https://image.tmdb.org/t/p/w500/" + movie.get('poster_path', '')
#
#             return title, overview, poster_url
#         else:
#             return movie_name, "No details found.", ""
#     except Exception as e:
#         return movie_name, f"Error fetching details: {str(e)}", ""
#
#
# # Function to get recommended movies
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     for i in movies_list:
#         movie_name = movies.iloc[i[0]].title
#         recommended_movies.append(movie_name)
#
#     return recommended_movies
#
#
# # Load Data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similar.pkl', 'rb'))
#
# # Streamlit UI Design
# st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
# st.title("🎥 Movie Recommender System")
#
# selected_movie_name = st.selectbox("Select a Movie to Get Recommendations", movies['title'].values)
#
# if st.button("Recommend"):
#     recommendations = recommend(selected_movie_name)
#
#     # Create a 2-column layout to display movies side by side
#     cols = st.columns(5)
#
#     for index, movie in enumerate(recommendations):
#         title, overview, poster_url = fetch_movie_details(movie)
#
#         with cols[index]:  # Assign each movie to a column
#             if poster_url:
#                 st.image(poster_url, width=200, caption=title)  # Display movie poster
#             st.markdown(f"**{title}**")  # Display movie title
#             st.caption(overview[:100] + "...")  # Display short description


    # import streamlit as st
    # import pandas as pd
    # import requests
    # import pickle
    #
    # # TMDb API Key (Replace with your own)
    # TMDB_API_KEY = "YOUR_TMDB_API_KEY"
    #
    #
    # # Function to fetch movie details (Poster, Title, Overview)
    # def fetch_movie_details(movie_name):
    #     try:
    #         # Make sure movie name is properly encoded
    #         search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={requests.utils.quote(movie_name)}"
    #         response = requests.get(search_url)
    #         data = response.json()
    #
    #         # Check if results exist
    #         if "results" in data and len(data["results"]) > 0:
    #             movie = data["results"][0]  # Get first search result
    #             title = movie.get("title", "Unknown")
    #             overview = movie.get("overview", "No description available.")
    #             poster_path = movie.get("poster_path")
    #
    #             # Construct the full poster URL
    #             if poster_path:
    #                 poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    #             else:
    #                 poster_url = "https://via.placeholder.com/200x300.png?text=No+Image"  # Placeholder for missing images
    #
    #             return title, overview, poster_url
    #         else:
    #             return movie_name, "No details found.", "https://via.placeholder.com/200x300.png?text=No+Image"
    #     except Exception as e:
    #         return movie_name, f"Error fetching details: {str(e)}", "https://via.placeholder.com/200x300.png?text=No+Image"
    #
    #
    # # Function to get recommended movies
    # def recommend(movie):
    #     movie_index = movies[movies['title'] == movie].index[0]
    #     distances = similarity[movie_index]
    #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    #
    #     recommended_movies = []
    #     for i in movies_list:
    #         movie_name = movies.iloc[i[0]].title
    #         recommended_movies.append(movie_name)
    #
    #     return recommended_movies
    #
    #
    # # Load Data
    # movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    # movies = pd.DataFrame(movies_dict)
    # similarity = pickle.load(open('similar.pkl', 'rb'))
    #
    # # Streamlit UI Design
    # st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
    # st.title("🎥 Movie Recommender System")
    #
    # selected_movie_name = st.selectbox("Select a Movie to Get Recommendations", movies['title'].values)
    #
    # if st.button("Recommend"):
    #     recommendations = recommend(selected_movie_name)
    #
    #     # Create a 2-column layout to display movies side by side
    #     cols = st.columns(5)
    #
    #     for index, movie in enumerate(recommendations):
    #         title, overview, poster_url = fetch_movie_details(movie)
    #
    #         with cols[index]:  # Assign each movie to a column
    #             st.image(poster_url, width=200, caption=title)  # Display movie poster
    #             st.markdown(f"**{title}**")  # Display movie title
    #             st.caption(overview[:100] + "...")  # Display short description
    #
    #


# import pandas as pd
# import streamlit as st
# import pickle
#
# # Load Data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similar.pkl', 'rb'))
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
#     return recommended_movies
#
# # Custom CSS for BETEGY-style UI
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(135deg, #1a1a2e, #16213e);
#             color: white;
#             font-family: 'Poppins', sans-serif;
#         }
#         .stApp {
#             background: linear-gradient(135deg, #1a1a2e, #16213e);
#             padding: 20px;
#         }
#         .title {
#             font-size: 50px;
#             font-weight: bold;
#             text-align: center;
#             color: #00d4ff;
#             text-transform: uppercase;
#             letter-spacing: 2px;
#         }
#         .subheader {
#             font-size: 22px;
#             text-align: center;
#             color: #b0bec5;
#             margin-bottom: 30px;
#         }
#         .stSelectbox {
#             background-color: #16213e;
#             color: white;
#             border-radius: 8px;
#         }
#         .stButton > button {
#             background: linear-gradient(90deg, #00d4ff, #0097e6);
#             color: white;
#             border: none;
#             font-size: 20px;
#             font-weight: bold;
#             padding: 12px 25px;
#             border-radius: 10px;
#             transition: 0.3s;
#         }
#         .stButton > button:hover {
#             background: linear-gradient(90deg, #0097e6, #00d4ff);
#             transform: scale(1.05);
#         }
#         .result-box {
#             background: linear-gradient(90deg, #0097e6, #00d4ff);
#             color: white;
#             padding: 15px;
#             border-radius: 12px;
#             font-size: 24px;
#             text-align: center;
#             font-weight: bold;
#             margin-top: 20px;
#             box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.5);
#         }
#     </style>
# """, unsafe_allow_html=True)
#
# # Title
# st.markdown("<h1 class='title'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
# st.markdown("<h3 class='subheader'>Find Your Next Favorite Movie!</h3>", unsafe_allow_html=True)
#
# # Movie Selection
# selected_movie_name = st.selectbox("Choose a Movie", movies['title'].values)
#
# # Recommendation Button
# if st.button("🎥 Recommend Movies"):
#     recommendations = recommend(selected_movie_name)
#     st.markdown("<div class='result-box'>Recommended Movies:</div>", unsafe_allow_html=True)
#     for movie in recommendations:
#         st.markdown(f"<div class='result-box'>{movie}</div>", unsafe_allow_html=True)





# import streamlit as st
# import pandas as pd
# import pickle
# import time
#
# # Load models and data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similar.pkl', 'rb'))
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
#     return recommended_movies
#
# # Custom CSS for Resn-like UI
# st.markdown("""
#     <style>
#         body {
#             background-color: black;
#             color: white;
#             font-family: 'Poppins', sans-serif;
#         }
#         .stApp {
#             background: black;
#         }
#         .title {
#             font-size: 50px;
#             font-weight: bold;
#             text-align: center;
#             color: #ff004c;
#             text-transform: uppercase;
#             letter-spacing: 2px;
#             animation: glow 1.5s infinite alternate;
#         }
#         @keyframes glow {
#             from { text-shadow: 0 0 5px #ff004c, 0 0 10px #ff004c; }
#             to { text-shadow: 0 0 20px #ff004c, 0 0 30px #ff004c; }
#         }
#         .stSelectbox, .stButton > button {
#             background-color: #222;
#             color: white;
#             border-radius: 8px;
#             transition: all 0.3s ease-in-out;
#         }
#         .stButton > button:hover {
#             background: linear-gradient(90deg, #ff004c, #ff7700);
#             transform: scale(1.1);
#         }
#         .movie-box {
#             background: linear-gradient(90deg, #ff004c, #ff7700);
#             color: white;
#             padding: 10px;
#             border-radius: 12px;
#             font-size: 20px;
#             text-align: center;
#             font-weight: bold;
#             margin-top: 20px;
#         }
#     </style>
# """, unsafe_allow_html=True)
#
# # Title
# st.markdown("<h1 class='title'>Movie Recommender System 🎬</h1>", unsafe_allow_html=True)
# selected_movie_name = st.selectbox("Choose a Movie", movies['title'].values)
#
# if st.button("Recommend 🚀"):
#     with st.spinner("Fetching Recommendations..."):
#         time.sleep(2)
#         recommendations = recommend(selected_movie_name)
#         for movie in recommendations:
#             st.markdown(f"<div class='movie-box'>{movie}</div>", unsafe_allow_html=True)



# import streamlit as st
# import pandas as pd
# import pickle
#
# # Load movie data and similarity matrix
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similar.pkl', 'rb'))
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     return [movies.iloc[i[0]].title for i in movies_list]
#
# # Custom CSS for a futuristic, Resn-inspired look
# st.markdown(
#     """
#     <style>
#         body {
#             background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
#             color: white;
#             font-family: 'Poppins', sans-serif;
#         }
#         .stApp {
#             background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
#             padding: 20px;
#         }
#         .title {
#             font-size: 60px;
#             font-weight: bold;
#             text-align: center;
#             color: #00d4ff;
#             text-transform: uppercase;
#             letter-spacing: 3px;
#             text-shadow: 0px 0px 10px rgba(0, 212, 255, 0.8);
#         }
#         .stSelectbox, .stButton > button {
#             background-color: #1a1a2e;
#             color: white;
#             border-radius: 10px;
#             font-size: 18px;
#         }
#         .stButton > button {
#             background: linear-gradient(90deg, #00d4ff, #0097e6);
#             padding: 12px 25px;
#             font-weight: bold;
#             border-radius: 12px;
#             transition: all 0.3s ease;
#         }
#         .stButton > button:hover {
#             background: linear-gradient(90deg, #0097e6, #00d4ff);
#             transform: scale(1.1);
#         }
#         .result-box {
#             background: rgba(255, 255, 255, 0.1);
#             border: 1px solid rgba(255, 255, 255, 0.3);
#             border-radius: 10px;
#             padding: 15px;
#             font-size: 22px;
#             text-align: center;
#             box-shadow: 0px 0px 20px rgba(0, 212, 255, 0.5);
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # Title
# st.markdown("<h1 class='title'>Movie Recommender System 🎬</h1>", unsafe_allow_html=True)
#
# # Movie selection dropdown
# selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)
#
# # Recommendation button
# if st.button("🔮 Recommend Movies"):
#     recommendations = recommend(selected_movie_name)
#     st.markdown("<div class='result-box'>", unsafe_allow_html=True)
#     for movie in recommendations:
#         st.markdown(f"<p style='font-size:20px; color:white;'>{movie}</p>", unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)


# import streamlit as st
# import pandas as pd
# import pickle
#
# # Load movie data and similarity matrix
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similar.pkl', 'rb'))
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     return [movies.iloc[i[0]].title for i in movies_list]
#
# # Custom CSS for a modern, cool, and professional look
# st.markdown(
#     """
#     <style>
#         body {
#             background: linear-gradient(145deg, #2c3e50, #34495e);  /* Dark gradient background */
#             font-family: 'Roboto', sans-serif;
#             color: white;
#             padding: 0;
#             margin: 0;
#         }
#         .stApp {
#             background: linear-gradient(145deg, #2c3e50, #34495e);  /* Dark gradient background */
#             padding: 40px;
#             max-width: 1200px;
#             margin: auto;
#             text-align: center;
#         }
#         .title {
#             font-size: 48px;
#             font-weight: 700;
#             color: #ffffff;
#             text-transform: uppercase;
#             margin-bottom: 40px;
#             letter-spacing: 2px;
#             text-shadow: 2px 2px 10px rgba(0, 204, 255, 0.6);  /* Cool glowing effect */
#         }
#         .stSelectbox {
#             width: 60%;
#             margin: auto;
#             font-size: 18px;
#             background-color: #34495e; /* Dark background for dropdown */
#             color: white;
#             padding: 12px 20px;
#             border-radius: 8px;
#             border: none;
#             transition: all 0.3s ease;
#         }
#         .stSelectbox:hover {
#             background-color: #2c3e50; /* Slightly darker on hover */
#         }
#         .stButton > button {
#             background: linear-gradient(45deg, #2980b9, #8e44ad); /* Gradient blue/purple buttons */
#             border-radius: 10px;
#             font-size: 18px;
#             font-weight: 600;
#             padding: 14px 30px;
#             color: white;
#             border: none;
#             cursor: pointer;
#             transition: all 0.3s ease;
#         }
#         .stButton > button:hover {
#             transform: scale(1.05);
#             background: linear-gradient(45deg, #8e44ad, #2980b9); /* Reverse gradient on hover */
#         }
#         .result-box {
#             background: rgba(255, 255, 255, 0.1);
#             border-radius: 10px;
#             padding: 20px;
#             margin-top: 40px;
#             box-shadow: 0px 10px 20px rgba(0, 204, 255, 0.4);
#             border: 1px solid rgba(255, 255, 255, 0.2);
#         }
#         .result-box p {
#             color: white;
#             font-size: 22px;
#             margin: 12px 0;
#             font-weight: 600;
#             line-height: 1.6;
#         }
#         .result-box p:first-child {
#             font-size: 24px;
#             font-weight: 700;
#             color: #00d4ff; /* Accent color for the main heading */
#         }
#         .header {
#             font-size: 30px;
#             font-weight: 600;
#             color: white;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .stSelectbox, .stButton > button {
#             transition: all 0.3s ease;
#         }
#         /* Animation for the movie recommendation list */
#         @keyframes fadeIn {
#             0% { opacity: 0; }
#             100% { opacity: 1; }
#         }
#         .result-box p {
#             animation: fadeIn 0.5s ease-out;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # Title
# st.markdown("<h1 class='title'>Movie Recommender System 🎬</h1>", unsafe_allow_html=True)
#
# # Movie selection dropdown
# selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)
#
# # Recommendation button
# if st.button("🔮 Recommend Movies"):
#     recommendations = recommend(selected_movie_name)
#     st.markdown("<div class='result-box'>", unsafe_allow_html=True)
#     st.markdown(f"<p class='header'>Recommended Movies for {selected_movie_name}</p>", unsafe_allow_html=True)
#     for movie in recommendations:
#         st.markdown(f"<p>{movie}</p>", unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)



import streamlit as st
import pandas as pd
import requests
import pickle

# TMDb API Key (Replace with your own)
TMDB_API_KEY = "a210d42061ac24e9a3ddee514a701ae7"

# Function to fetch movie details (Poster, Title, Overview)
def fetch_movie_details(movie_name):
    try:
        # Search for the movie in TMDb
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}"
        response = requests.get(search_url)
        data = response.json()

        # Check if results exist
        if data['results']:
            movie = data['results'][0]  # Get first search result
            title = movie.get('title', 'Unknown')
            overview = movie.get('overview', 'No description available.')
            poster_url = "https://image.tmdb.org/t/p/w500/" + movie.get('poster_path', '')

            return title, overview, poster_url
        else:
            return movie_name, "No details found.", "https://via.placeholder.com/200x300.png?text=No+Image"
    except Exception as e:
        return movie_name, f"Error fetching details: {str(e)}", "https://via.placeholder.com/200x300.png?text=No+Image"

# Function to get recommended movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_name = movies.iloc[i[0]].title
        recommended_movies.append(movie_name)

    return recommended_movies

# Load Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similar.pkl', 'rb'))

# Streamlit UI Design
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎥 Movie Recommender System")

selected_movie_name = st.selectbox("Select a Movie to Get Recommendations", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    # Create a 2-column layout to display movies side by side
    cols = st.columns(5)

    for index, movie in enumerate(recommendations):
        title, overview, poster_url = fetch_movie_details(movie)

        with cols[index]:  # Assign each movie to a column
            if poster_url:
                st.image(poster_url, width=200, caption=title)  # Display movie poster
            st.markdown(f"**{title}**")  # Display movie title
            st.caption(overview[:100] + "...")  # Display short description
