import streamlit as st
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Sentiment Analysis System",page_icon="https://static.thenounproject.com/png/3383089-200.png")
st.title("SENTIMENT ANALYSIS SYSTEM")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/9850/9850903.png")
choice=st.sidebar.selectbox("My Menu",("HOME","ANALYZE SENTIMENT","VISUALIZE THE RESULTS"))
if(choice=="HOME"):
    st.image("https://i.pinimg.com/originals/52/ad/6a/52ad6a11c1dcb1692ff9e321bd520167.gif")
    st.markdown("<center><h1>WELCOME</h1></center>",unsafe_allow_html=True)
elif(choice=="ANALYZE SENTIMENT"):
    url=st.text_input("Enter Google Sheet URL")
    r=st.text_input("Enter range:")
    c=st.text_input("Enter Column")
    btn=st.button("ANALYZE")
    if btn:
        if 'cred' not in st.session_state:
            f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
            st.session_state['cred']=f.run_local_server(port=0)
        mymodel=SentimentIntensityAnalyzer()
        service=build('Sheets','v4',credentials=st.session_state['cred']).spreadsheets().values()
        d=service.get(spreadsheetId=url,range=r).execute()
        mycolumns=d['values'][0]
        mydata=d['values'][1:]
        df=pd.DataFrame(data=mydata,columns=mycolumns)
        l=[]
        for i in range(0,len(df)):
            k=df._get_value(i,c)
            pred=mymodel.polarity_scores(k)
            if(pred['compound']>0.5):
                l.append("Positive")
            elif(pred['compound']<-0.5):
                l.append("Negative")
            else:
                l.append("Neutral")
        df['Sentiments']=l
        st.dataframe(df)
        df.to_csv("Review.csv",index=False)
        st.header("This data has been saved by the name of review.csv")
elif(choice=="VISUALIZE THE RESULTS"):
    choice2=st.selectbox("Choose Visualization:",("None","Pie","Histogram"))
    if(choice2=="Pie"):
        df=pd.read_csv("Review.csv")
        prosper=(len(df[df['Sentiments']=='Positive'])/len(df))* 100
        negper= (len(df[df['Sentiments']=='Negative'])/len(df))* 100
        neuper= (len(df[df['Sentiments']=='Neutral'])/len(df))* 100
        fig=px.pie(values=[prosper,negper,neuper],names=['Positive','Negative','Neutral'])
        st.plotly_chart(fig)
    elif(choice2=="Histogram"):
        t=st.text_input("Choose any Categorical column")
        if t:
            df=pd.read_csv("Review.csv")
            fig=px.histogram(x=df['Sentiments'],color=df[t])
            st.plotly_chart(fig)
            



