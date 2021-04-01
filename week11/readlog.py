# This program reads in a log file
# Author: Sarah McNelis

import pandas as pd

#path = './data/'
logFilename = 'access.log' #path + 'access.log'

#need column names to give meaning
colNames= ('ip',
    'dash1', 
    'userId', 
    'time', 
    'url', 
    'status code', 
    'size of response', 
    'referer', 
    'user agent', 
    'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

print(df)

# To drop columns that contain justt dashes
# Do not run incase webserver is set up for userIds!! 
#df.drop(columns=['dash1', 'userId'], inplace=True)

# remove the [] from time
# apply the function to each element in the column and return a series
df['time'] = df['time'].applu(lambda x: re.search('[w:/]+', x).group())

'''
# FYI for the task use a normal function instead of lambda
def getNewValue(x):
    newvalue = re.search('[\w:/]+', x).group()
    # do your stuff
    return newvalue
df['time'] = df['time'].apply(getNewValue)
'''
# this is not a normal date time format so need to specify it
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html?highlight=to_datetime
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
print (df.dtypes)
# output row of id 0
print(df.iloc[0])

start_date = pd.to_datetime('2021/02/15 23:00')
end_date = pd.to_datetime('2021/02/15 23:59:59')

# see below for more info on dealing with time
# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/09_timeseries.html
# way one use the loc function: newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]
# way 2 use the series function between: newdf = df[df.time.between(start_date, end_date)]
# way three set the index to the date column
# this give a whole pile of handy features
df = df.set_index(['time'])
newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
#newdf = df.between_time('23:00', '23:59') # this is times every day
print (newdf)

# sample the download sizes say every 30 Minutes
downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)

# ok I cheated a bit here
# more information on the documents
# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/04_plotting.html
downloadSamples.plot()
plt.show()