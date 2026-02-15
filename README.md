#  Movie Recommender System

A content-based machine learning web application that recommends movies based on user preferences. Built with Python and Streamlit, this system analyzes movie metadata to find similarities and uses the TMDB API to fetch dynamic movie posters.

##  Features
* **Content-Based Filtering:** Recommends the top 5 most similar movies based on tags, genres, cast, and crew.
* **Dynamic Posters:** Connects to the TMDB API to fetch and display high-resolution movie posters in real-time.
* **Interactive UI:** A clean, easy-to-use web interface built entirely in Python using Streamlit.

##  Architecture & How It Works
1. **Data Preprocessing:** The system cleans and merges the TMDB 5000 Movies and Credits datasets, extracting key text features.
2. **Vectorization:** Text data is stemmed and converted into vectors.
3. **Similarity Calculation:** A cosine similarity matrix is calculated to find the mathematical distance between different movies.
4. **Web App:** The Streamlit interface loads the pre-computed similarity matrix and queries the TMDB API for visual assets.

##  Tech Stack
* **Language:** Python
* **Frontend/Framework:** Streamlit
* **Machine Learning:** Scikit-Learn (Cosine Similarity), Pandas, NumPy
* **External APIs:** The Movie Database (TMDB) API
* **Deployment:** Streamlit Community Cloud
