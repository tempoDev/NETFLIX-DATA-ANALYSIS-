import pandas as pd
import matplotlib.pyplot as plt

nf = pd.read_csv("./files/netflix_titles.csv")

# Distribucion de tipos 
n_movies = nf[nf['type'] == 'Movie'].shape
n_tvshows = nf[nf['type'] == 'TV Show'].shape


labels = ['Movies', 'TV Shows']
sizes = [n_movies[0], n_tvshows[0]]

#print(f"Number of Movies: {n_movies[0]}")
#print(f"Number of TV Shows: {n_tvshows[0]}")

fig, ax = plt.subplots()
ax.pie(sizes, labels= labels, autopct='%1.1f%%', startangle=90)
#---------------------------------------------------------------

# Distribucion por año de lanzamiento
fig, ax = plt.subplots()
n_years = nf['release_year'].value_counts().sort_index() 
#print(f"Number of Unique Release Years: {n_years}")
ax.hist(nf['release_year'], bins=n_years.shape[0] ,color='skyblue', edgecolor='black')
ax.set_title('Distribution of Release Years for Netflix Titles')
#---------------------------------------------------------------

# Distribución por década

fig, ax = plt.subplots()
nf['decade'] = (nf['release_year'] // 10) * 10
d_decade = nf['decade'].value_counts().sort_index()

ax.bar(d_decade.index.astype(str), d_decade.values, color='salmon', edgecolor='black')
ax.set_title('Distribution of Netflix Titles by Decade')
#---------------------------------------------------------------

# Top 10 paises con mas titulos
d_country = nf['country'].value_counts().head(10)
fig, ax = plt.subplots()
ax.bar(d_country.index, d_country.values, color='lightgreen', edgecolor='black' )

total = d_country.values.sum()
for i, v in enumerate(d_country.values):
    pct = v / total * 100
    ax.text(i, v, f'{v}\n({pct:.1f}%)', ha='center', va='bottom')
    
ax.set_title('Top 10 Countries by Number of Netflix Titles')
ax.set_ylabel('Number of Titles')
ax.set_xlabel('Country')

genres = nf['listed_in'].str.split(', ', expand=True).stack()
#print(genres.value_counts().head(10))

fig, ax = plt.subplots()
ax.pie(genres.value_counts().head(10), labels=genres.value_counts().head(10).index, autopct='%1.1f%%', startangle=90)
#---------------------------------------------------------------

# Duración promedio por década

fig, ax = plt.subplots()
nf_movies = nf[nf['type'] == 'Movie'].copy()
nf_movies['duration'] = pd.to_numeric(nf_movies['duration'].str.replace(' min', ''), errors='coerce')
avg_duration_by_decade = nf_movies.groupby('decade')['duration'].mean() 

ax.bar(avg_duration_by_decade.index.astype(str), avg_duration_by_decade.values, color='orchid', edgecolor='black')
ax.set_title('Average Movie Duration by Decade')    
#---------------------------------------------------------------

plt.show()