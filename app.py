import streamlit as st
import pandas as pd
import yfinance as yf
import requests
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# --- 1. CONFIG & REFRESH ENGINE ---
st.set_page_config(page_title="2026 Global Intelligence", layout="wide")
st_autorefresh(interval=60 * 1000, key="global_refresh")

# --- 2. LIVE API CONNECTORS ---

@st.cache_data(ttl=60)
def fetch_macro():
    """Live Tickers via Yahoo Finance."""
    tickers = {"S&P 500": "^GSPC", "Gold": "GC=F", "BTC": "BTC-USD", "Copper": "HG=F", "Nvidia": "NVDA"}
    data = {}
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym).history(period="1d")
            data[name] = {"price": t["Close"].iloc[-1], "change": ((t["Close"].iloc[-1] - t["Open"].iloc[-1]) / t["Open"].iloc[-1]) * 100}
        except: data[name] = {"price": 0.0, "change": 0.0}
    return data

@st.cache_data(ttl=300)
def fetch_whale_signals():
    """Live Prediction Market Data via Polymarket Gamma API."""
    try:
        # Fetching latest event data for Midterms and Fed
        # Endpoint: https://gamma-api.polymarket.com/events
        res = requests.get("https://gamma-api.polymarket.com").json()
        return res
    except: return []

@st.cache_data(ttl=900)
def fetch_censorship_status():
    """Live Network Interference via OONI API."""
    try:
        # OONI provides real-time measurement data
        res = requests.get("
