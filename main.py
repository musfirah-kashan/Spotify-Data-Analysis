import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('spotify.csv')
print(df.columns.tolist())
# print(df)
#top 10 artists and top 10 genres data
top_artists = df['artists'].value_counts().head(10)
top_genres_pop = df.groupby('track_genre')['popularity'].mean().nlargest(10)
fig,ax=plt.subplots(1,2,figsize=(14,6))
ax[0].barh(top_artists.index[::-1], top_artists.values[::-1], color='skyblue')
ax[0].set_title('Top 10 Artists by Track Count', fontsize=12, fontweight='bold')
ax[0].set_xlabel('Number of Tracks')
ax[0].set_ylabel('Artist Name')

ax[1].barh(top_genres_pop.index[::-1], top_genres_pop.values[::-1], color='lightgreen')
ax[1].set_title('Top 10 Most Frequent Genres', fontsize=12, fontweight='bold')
ax[1].set_xlabel('Number of Tracks')
ax[1].set_ylabel('Genre')

fig.suptitle('Spotify Artist & Genre Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('graphs/artists_and_genre_distribution.png',dpi=300,bbox_inches='tight')
plt.show()