import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

# 1. Page Configuration
st.set_page_config(page_title="2026 Global Macro Hub", layout="wide")

# 2. AUTO-REFRESH ENGINE (60 Seconds)
st_autorefresh(interval=60 * 1000, key="data_refresh")

st.title("🌐 2026 Global Macro & Signal Dashboard")
st.caption(f"Real-time data aggregation: February 8, 2026 | Last Refresh: {pd.Timestamp.now().strftime('%H:%M:%S')}")

# 3. LIVE MACRO ORACLE
@st.cache_data(ttl=60)
def fetch_live_macro():
    """Fetches live market benchmarks from 
