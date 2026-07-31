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

# Audio Feature Trends Over Time 
# df['duration_min']=df['duration_ms']/60000
# yearly_trends=df.groupby('year')[['duration_min','energy','loudness']].mean()
# fig,ax=plt.subplots(1,2,figsize=(14,5))
# ax[0].plot(yearly_trends.index,yearly_trends['duration_min'],color='purple',linewidth=2)
# ax[0].set_title('Average Song Duration Over Time', fontsize=12, fontweight='bold')
# ax[0].set_xlabel('Release Year')
# ax[0].set_ylabel('Duration(Mins)')
# ax[0].grid(color='gray',linestyle='--')

# ax[1].plot(yearly_trends.index,yearly_trends['energy'],color='orange',linewidth=2)
# ax[1].set_title('Evolution of Energy Over Time',fontsize=12,fontweight='bold')
# ax[1].set_xlabel('Release Year')
# ax[1].set_ylabel('Average Energy Score')
# ax[1].grid(color='gray',linestyle='--')

# fig.suptitle('Spotify Audio Feature Trends Over Time', fontsize=14, fontweight='bold')
# plt.tight_layout()
# # plt.savefig('graphs/audio_feature_trends_over_time.png', dpi=300, bbox_inches='tight')
# plt.show()

#explicit vs non explicit songs
explicit_songs=df['explicit'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(explicit_songs,labels=['Explicit','Non Explicit'],autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'],startangle=90,explode=(0, 0.1))
plt.title('Explicit Content Distribution', fontweight='bold')
plt.tight_layout()
plt.savefig('graphs/explicit_vs_non-explicit_songs.png', dpi=300, bbox_inches='tight')
plt.show()

#Top 10 tracks
top_tracks=df.sort_values(by='popularity',ascending=False).drop_duplicates('track_name').head(10)
plt.figure(figsize=(10,5))
plt.barh(top_tracks['track_name'][::-1],top_tracks['popularity'][::-1],color='purple')
plt.title('Top 10 Most Popular Tracks', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Track Name')
plt.tight_layout()
plt.savefig('graphs/top_tracks.png', dpi=300, bbox_inches='tight')
plt.show()

top_artists=df.groupby('artists')['popularity'].mean().nlargest(10)
plt.figure(figsize=(10,5))
plt.barh(top_artists.index[::-1],top_artists.values[::-1],color='teal')
plt.title('Top 10 Popular Artists', fontweight='bold')
plt.xlabel('Popularity Score')
plt.ylabel('Artists Name')
plt.tight_layout()
plt.savefig('graphs/top_artists.png', dpi=300, bbox_inches='tight')
plt.show()
