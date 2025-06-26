import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
games = pd.read_csv('games.csv')

# Convert descriptions to TF-IDF vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(games['Description'])

# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Game title to index mapping
indices = pd.Series(games.index, index=games['Title']).drop_duplicates()

# Recommendation function
def recommend(title, num=5):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num+1]
    game_indices = [i[0] for i in sim_scores]
    return games['Title'].iloc[game_indices]
