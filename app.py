# app.py
import streamlit as st
import pandas as pd
from recommender import recommend, games

st.title("🎮 Game Recommender App")
st.write("Find similar games based on your favorite!")

# Dropdown menu
game_list = games['Title'].values
selected_game = st.selectbox("Choose a game:", game_list)

# Show recommendations
if st.button("Recommend"):
    st.subheader("You might also like:")
    recommendations = recommend(selected_game)
    for game in recommendations:
        st.write("🔹", game)
