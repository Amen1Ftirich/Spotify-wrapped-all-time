from combined_data import totaldata
import pandas as pd

time_sort_artist =  totaldata.sort_values(by='ms_played', ascending=False, ignore_index=True)
print(time_sort_artist)
artist_id = totaldata['master_metadata_album_artist_name'].value_counts().idxmax()

total_time_listened_hours = totaldata['ms_played'].sum()* 1.66667e-5 //60
total_time_listened_minutes = totaldata['ms_played'].sum()* 1.66667e-5 %60
track_id = totaldata['master_metadata_track_name'].value_counts().idxmax()
album_id = totaldata['master_metadata_album_album_name'].value_counts().idxmax()


def find_artist (dataframe, item_name, item_column):
    matching_rows = dataframe[dataframe[item_column] == item_name]

    #js in case
    if matching_rows.empty:
        return None
    corresponding_artist = (
        matching_rows["master_metadata_album_artist_name"].value_counts().idxmax()
    
    )
    return corresponding_artist
def find_time(dataframe,item_name,item_column)



print(f"Your most listened to artist is {artist_id}")
print(f"Your most listened to album is {album_id} by {find_artist(totaldata,album_id,"master_metadata_album_album_name")}")
print(f"Your most listened to track is {track_id} by {find_artist(totaldata,track_id,"master_metadata_track_name")}")
print(f"you listened to music for {total_time_listened_hours} hours and {total_time_listened_minutes} minutes")