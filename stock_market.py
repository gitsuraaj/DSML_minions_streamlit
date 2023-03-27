import streamlit as st
import yfinance as yf
import datetime

st.header('Stock Market Analyser')



#textbox
ticker_symbol= st.text_input("Enter stock Symbol",
                             "AAPL",
                             key="placeholder")
ticker_data= yf.Ticker(ticker_symbol)

#date input

col1, col2= st.columns(2)

with col1:
   st.header("Starting Date")
   start_date=st.date_input(
       "Input Starting date",
       datetime.date(2019, 1, 1))

with col2:
   st.header("Ending Date")
   end_date=st.date_input(
       "Input Ending date",
       datetime.date(2022, 12, 31))



ticker_df = ticker_data.history(period="1d", start=f'{start_date}', end=f'{end_date}')
dicter= {'AAPL': "APPLE", 'GOOG': "Google"}





st.write(f"""
         {dicter[ticker_symbol]} stock price analysis: 
         
         """)
st.dataframe(ticker_df)

#linechart inside layouts and containers

col1, col2= st.columns(2)

with col1:
   st.header("Volume Analysis")
   st.line_chart(ticker_df['Volume'])

with col2:
   st.header("Closing Price Analysis")
   st.line_chart(ticker_df['Close'])






