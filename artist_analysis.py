from combined_data import totaldata
import pandas as pd

time_sort_artist =  totaldata.sort_values(by='ms_played', ascending=False)
print(time_sort_artist)