import pandas as pd
import glob

allfiles = glob.glob('data/Streaming_History_Audio_*.json')
df_allfiles = pd.concat((pd.read_json(f) for f in allfiles), ignore_index=True)
alldataframed = pd.DataFrame(df_allfiles)
print(alldataframed.info())