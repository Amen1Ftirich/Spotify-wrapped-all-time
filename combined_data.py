import pandas as pd
import glob
import pylance as pl

allfiles = glob.glob('data/Streaming_History_Audio_*.json')
df_allfiles = pd.concat((pd.read_json(f) for f in allfiles), ignore_index=True)
alldataframed = pd.DataFrame(df_allfiles)
columns_to_drop = [
    "ts",
    "platform",
    "conn_country",
    "ip_addr",
    "spotify_track_uri",
    "episode_name",
    "episode_show_name",
    "spotify_episode_uri",
    "reason_start",
    "reason_end",
    "shuffle",
    "skipped",
    "offline",
    "offline_timestamp",
    "incognito_mode",
    "audiobook_title",
    "audiobook_uri",
    "audiobook_chapter_uri",
    "audiobook_chapter_title",

]
totaldata = df_allfiles.drop(columns= columns_to_drop)
ms_remove = totaldata[totaldata["ms_played"] = 0]
print(totaldata)