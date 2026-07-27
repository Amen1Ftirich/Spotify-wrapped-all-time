import glob as glob
import pandas as pd
from combined_data import totaldata
selected_year = int(input("Which year do you want to get data from?"))
#converting ts to clear time stamps:
totaldata['ts'] = pd.to_datetime(totaldata['ts'], utc= True)
totaldata["year"] = totaldata['ts'].dt.year
totaldata["month"] = totaldata['ts'].dt.month_name()
totaldata["day"] = totaldata['ts'].dt.day

def get_year_data(dataframe, year):
    filtered_data = dataframe[dataframe['year'] == selected_year ].copy()
    if filtered_data.empty:
        return None
    return filtered_data
year_Data = get_year_data(totaldata, selected_year)
artist_id_year = year_Data['master_metadata_album_artist_name'].value_counts().idxmax()
album_id_year = year_Data['master_metadata_album_album_name'].value_counts().idxmax()
track_id_year = year_Data['master_metadata_track_name'].value_counts().idxmax()



print(f"Your top artist in {selected_year} is {artist_id_year}")
print(f"Your top track in {selected_year} is {track_id_year}")
print(f"Your top album in {selected_year} is {album_id_year}")
    