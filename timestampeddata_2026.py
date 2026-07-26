import glob as glob
import pandas as pd
from combined_data import totaldata
#year_need = int(input("Which year do you want to get data from?"))
#converting ts to clear time stamps:
totaldata['ts'] = pd.to_datetime(totaldata['ts'], utc= True)
print(totaldata)
totaldata["year"] = totaldata['ts'].dt.year
totaldata["month"] = totaldata['ts'].dt.month_name()
totaldata["day"] = totaldata['ts'].dt.day
print(totaldata.head(10))