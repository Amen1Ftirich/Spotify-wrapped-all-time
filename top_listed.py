from combined_data import totaldata
import pandas as pd

# this will list the top 10 artists, albums, tracks based on reaccurance

artist_data = totaldata["master_metadata_album_artist_name"].value_counts(ascending= False, sort= True)
top_10_artists = artist_data.head(10).rename_axis("artist").reset_index(name = "play_count")
album_data = totaldata[["master_metadata_album_album_name", "master_metadata_album_artist_name"]].value_counts(ascending= False, sort= True)
top_10_albums =(album_data.head(10).reset_index(name = "play_count"))
top_10_albums.index += 1
top_10_artists.index += 1
track_data = totaldata[["master_metadata_track_name", "master_metadata_album_artist_name"]].value_counts(ascending=False, sort = True)
top_10_tracks = (track_data.head(10).reset_index(name="play counts"))



print(top_10_tracks)
print(top_10_albums)
#print(top_10_artists)