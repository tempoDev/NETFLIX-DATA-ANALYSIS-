import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

nf = pd.read_csv("./files/netflix_titles.csv")

nf = nf.drop_duplicates(subset='title').reset_index(drop=True)

print(nf)

nf = nf.dropna(subset=['description'])
nf = nf.reset_index(drop=True)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(nf['description'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(title, n=10, cosine_sim=cosine_sim):
    idx = nf[nf['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]  # quitar la propia
    movie_indices = [i[0] for i in sim_scores]
    return nf['title'].iloc[movie_indices]

print(recommend("Stranger Things"))