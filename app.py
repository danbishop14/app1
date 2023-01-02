import pandas as pd
import streamlit as st
import yfinance as yf

ticker  = yf.Ticker('AAPL')

@st.cache
def get_df() -> pd.DataFrame:
    ticker = yf.Ticker('AAPL')
    df = ticker.history(period='10y')
    return df
df = get_df()

st.title('site')
st.dataframe(df.tail(400))

