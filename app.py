import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Market Data Dashboard", layout="wide")

# --- LIVE DATA FETCHING ---
@st.cache_data(ttl=60*60*24) # Cache data for 24 hours
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC",
        "Dow Jones": "^DJI",
        "Nasdaq": "^IXIC",
        "Gold": "GC=F",
        "Bitcoin": "BTC-USD"
    }
    results = {}
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym).history(period="1d")
            if not t.empty:
                results[name] = {
                    "price": t["Close"].iloc[-1],
                    "change": ((t["Close"].iloc[-1] - t["Open"].iloc[-1]) / t["Open"].iloc[-1]) * 100 if "Open" in t.columns else 0
                }
        except Exception as e:
            st.error(f"Error fetching data for {name} ({sym}): {e}")
            results[name] = {"price": 0.0, "change": 0.0}
    return results

live_data = fetch_market_data()

# --- MAIN INTERFACE ---
st.title("Market Data Dashboard")
st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Display metrics
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with col2:
    st.metric("Dow Jones", f"{live_data['Dow Jones']['price']:,.2f}", f"{live_data['Dow Jones']['change']:.2f}%")
with col3:
    st.metric("Nasdaq", f"{live_data['Nasdaq']['price']:,.2f}", f"{live_data['Nasdaq']['change']:.2f}%")
with col4:
    st.metric("Gold", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with col5:
    st.metric("Bitcoin", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")

st.divider()

st.write("This is a basic dashboard to display current market data.")

