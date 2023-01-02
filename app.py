import pandas as pd
import streamlit as st
import yfinance as yf


st.title('simple_test_site')

#Full Data Caching
url = "https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"
@st.cache
def get_data() -> pd.DataFrame:
    return pd.read_csv(url, compression='gzip', sep='\t')
df = get_data()

st.dataframe(df.tail(1000))

# ticker  = yf.Ticker('AAPL')

# #Full Data Caching
# @st.cache
# def get_data() -> pd.DataFrame:
#     url = "https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"
#     return pd.read_csv(url, compression='gzip', sep='\t')
# df1 = get_data()


# @st.cache
# def get_df() -> pd.DataFrame:
#     ticker = yf.Ticker('AAPL')
#     df = ticker.history(period='10y')
#     return df
# df = get_df()

# st.title('site')
# st.dataframe(df.tail(400))

