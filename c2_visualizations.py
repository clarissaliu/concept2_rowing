import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

all_data = pd.read_csv('all_data.csv', index_col=0, converters={'age':int, 'rank':int})




#times = all_data['time'].str.replace('.',':')
#ms_time_split = times.str.rsplit(':',1,expand=True)
#milliseconds = ms_time_split[1]

#s_time_split = ms_time_split[0].str.rsplit(':',1,expand=True)
#seconds = s_time_split[1]
#seconds.loc[seconds.str.len()<2] = '0'+seconds

#min_time_split = s_time_split[0].str.rsplit(':',1,expand=True)
#minutes = pd.DataFrame(min_time_split,columns=[1])
#minutes.loc[minutes.str.len()<2] = '0'+minutes
#minutes.loc[minutes[1].isnull(), 1] = '00'

#hours = min_time_split[0]
#hours.loc[hours.str.len()<2] = '0'+hours

#hm = hours.str.cat(minutes,sep=':')
#hms = hm.str.cat(seconds,sep=':')
#new_time = hms.str.cat(milliseconds,sep='.')
#all_data['new time'] = new_time


#time_datetime = pd.to_datetime(all_data['new time'],format='%H:%M:%S:%f')

#minutes = min_time_split[1]
#hours = min_time_split[0]



#print(seconds)
#print(minutes)
#print(hours)

female_data = all_data[all_data['gender']=='female']
male_data = all_data[all_data['gender']=='male']
data_100m = all_data[all_data['distance']==100]
data_500m = all_data[all_data['distance']== 500]
data_1000m = all_data[all_data['distance']== 1000]
data_2000m = all_data[all_data['distance']== 2000]
data_5000m = all_data[all_data['distance']== 5000]
data_6000m = all_data[all_data['distance']== 6000]
data_10000m = all_data[all_data['distance']== 10000]
data_21097m = all_data[all_data['distance']== 21097]
data_42195m = all_data[all_data['distance']== 42195]
data_100000m = all_data[all_data['distance']== 100000]


print(all_data.head())

#print(times.head())


#sns.relplot(x='age',y='rank',data=top_500_male, hue='distance')
#plt.savefig('top500.png')

#sns.countplot(x='gender',data=all_data)
#plt.savefig('test2.png')