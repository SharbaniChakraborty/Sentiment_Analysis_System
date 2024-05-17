from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd
#Permission
f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
cred=f.run_local_server(port=0)
#create a service
service=build('Sheets','v4',credentials=cred).spreadsheets().values()
#Retrive data from Google Sheets
d=service.get(spreadsheetId='***************',range='A1:H').execute()
mycolumns=d['values'][0]
mydata=d['values'][1:]
df=pd.DataFrame(data=mydata,columns=mycolumns)
for i in range(0,len(df)):
    k=df._get_value(i,'Please leave your honest opinion about our product used recently by you.')
    print(k)


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
mymodel=SentimentIntensityAnalyzer()
pred=mymodel.polarity_scores("I love pizza!!!")
print(pred)
'''
#Permission
f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
cred=f.run_local_server(port=0)
#create a service
service=build('Sheets','v4',credentials=cred).spreadsheets().values()
#Retrive data from Google Sheets
d=service.get(spreadsheetId='*****************************',range='A1:H').execute()
mycolumns=d['values'][0]
mydata=d['values'][1:]
df=pd.DataFrame(data=mydata,columns=mycolumns)
for i in range(0,len(df)):
    k=df._get_value(i,'Opinion')
    print(k)
'''


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
mymodel=SentimentIntensityAnalyzer()
mymodel
#Permission
f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
cred=f.run_local_server(port=0)
#create a service
service=build('Sheets','v4',credentials=cred).spreadsheets().values()
#Retrive data from Google Sheets
d=service.get(spreadsheetId='**********************',range='A1:H').execute()
mycolumns=d['values'][0]
mydata=d['values'][1:]
df=pd.DataFrame(data=mydata,columns=mycolumns)
l=[]
for i in range(0,len(df)):
    k=df._get_value(i,'Opinion')
    pred=mymodel.polarity_scores(k)
    if(pred['compound']>0.5):
        l.append("Positive")
    elif(pred['compound']<0.5):
        l.append("Negative")
    else:
        l.append("Neutral")
df['Sentiments']=l
df.to_csv("Review.csv",index=False)


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
mymodel=SentimentIntensityAnalyzer()
mymodel
#Permission
f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
cred=f.run_local_server(port=0)
#create a service
service=build('Sheets','v4',credentials=cred).spreadsheets().values()
#Retrive data from Google Sheets
d=service.get(spreadsheetId='**************************',range='A1:B').execute()
mycolumns=d['values'][0]
mydata=d['values'][1:]
df=pd.DataFrame(data=mydata,columns=mycolumns)
l=[]
for i in range(0,len(df)):
    k=df._get_value(i,'Review')
    pred=mymodel.polarity_scores(k)
    if(pred['compound']>0.5):
        l.append("Positive")
    elif(pred['compound']<-0.5):
        l.append("Negative")
    else:
        l.append("Neutral")
df['Sentiments']=l
df.to_csv("Review.csv",index=False)


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
mymodel=SentimentIntensityAnalyzer()
mymodel
#Permission
f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
cred=f.run_local_server(port=0)
#create a service
service=build('Sheets','v4',credentials=cred).spreadsheets().values()
#Retrive data from Google Sheets
d=service.get(spreadsheetId='*******************************',range='A1:B').execute()
mycolumns=d['values'][0]
mydata=d['values'][1:]
df=pd.DataFrame(data=mydata,columns=mycolumns)
pos=0
neg=0
neu=0
for i in range(0,len(df)):
    k=df._get_value(i,'Review')
    pred=mymodel.polarity_scores(k)
    if(pred['compound']>0.5):
        pos=pos+1
    elif(pred['compound']<-0.5):
        neg=neg+1
    else:
        neu=neu+1

prosper=(pos/len(df))*100
negper=(neg/len(df))*100
neuper=(neu/len(df))*100
print("Positive:",prosper)
print("Negative:",negper)
print("Neutral:",neuper)


from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px
mymodel=SentimentIntensityAnalyzer()
mymodel
#Permission
f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
cred=f.run_local_server(port=0)
#create a service
service=build('Sheets','v4',credentials=cred).spreadsheets().values()
#Retrive data from Google Sheets
d=service.get(spreadsheetId='****************************',range='A1:B').execute()
mycolumns=d['values'][0]
mydata=d['values'][1:]
df=pd.DataFrame(data=mydata,columns=mycolumns)
pos=0
neg=0
neu=0
for i in range(0,len(df)):
    k=df._get_value(i,'Review')
    pred=mymodel.polarity_scores(k)
    if(pred['compound']>0.5):
        pos=pos+1
    elif(pred['compound']<-0.5):
        neg=neg+1
    else:
        neu=neu+1

prosper=(pos/len(df))*100
negper=(neg/len(df))*100
neuper=(neu/len(df))*100
print("Positive:",prosper)
print("Negative:",negper)
print("Neutral:",neuper)
fig=px.pie(values=[prosper,negper,neuper],names=['Positive','Negative','Neutral'])
fig.show()

