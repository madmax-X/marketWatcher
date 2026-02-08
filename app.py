import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import numpy as np

# --- 1. PAGE CONFIG & REFRESH ---
st.set_page_config(page_title="2026 Truth Oracle", layout="wide")
# Refresh every 60 seconds
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. ROBUST DATA FETCHING (Fixed for Weekend/Closed Markets) ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC",
        "Gold": "GC=F",
        "Bitcoin": "BTC-USD",
        "Copper": "HG=F",
        "Asia Index": "EEMA" # Foreign Signal
    }
    results = {}
    for name, sym in tickers.items():
        try:
            # Use period="5d" to ensure we get data even on weekends/holidays
            t = yf.Ticker(sym).history(period="5d")
            if not t.empty:
                current_price = t["Close"].iloc[-1]
                prev_price = t["Close"].iloc[-2] if len(t) > 1 else current_price
                change = ((current_price - prev_price) / prev_price) * 100
                results[name] = {"price": current_price, "change": change}
            else:
                results[name] = {"price": 0.0, "change": 0.0}
        except Exception:
            results[name] = {"price": 0.0, "change": 0.0}
    
    # Safety Check: Ensure every key exists to prevent KeyErrors
    for name in tickers.keys():
        if name not in results:
            results[name] = {"price": 0.0, "change": 0.0}
            
    return results

live_data = fetch_market_data()

# --- 3. MAIN INTERFACE ---
st.title("🌐 2026 Global Truth Oracle")
st.caption(f"Last Sync: {datetime.now().strftime('%H:%M:%S')} | Feb 8, 2026 (Weekend Pulse)")

# Metric Row (Now Safe from KeyErrors)
c1, c2, c3, c4 = st.columns(4)
c1.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
c2.metric("Gold Spot", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
c3.metric("Bitcoin", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
c4.metric("Copper", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

st.divider()

# --- 4. TRUTH VS. NARRATIVE MAP ---
st.header("🗺️ Geopolitical Truth Map & Information Sovereignty")
# Terrestrial Nodes & Satellite Slots
map_df = pd.DataFrame({
    'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31, 25.03, 10.0],
    'lon': [-74.00, -0.12, 103.81, -77.03, 116.40, 114.16, 121.56, 12.4],
    'Type': ['Node', 'Node', 'Node', 'Control', 'Control', 'Node', 'Kinetic', 'Orbital Drift']
})
st.map(map_df)

# --- 5. NARRATIVE DISCORDANCE TABLE ---
st.header("⚖️ Narrative Discordance Tracker (Foreign vs. Domestic)")
discord_df = pd.DataFrame({
    "Sector": ["Labor Market", "Energy Grid", "AI Hardware", "Global Trade"],
    "US Narrative (Domestic)": ["'Full Employment'", "'Green Transition'", "'Unlimited Growth'", "'Diversification'"],
    "Global Reality (Foreign)": ["$500k WaPo Relief fund", "17% Power Deficit", "HBM Memory 'Sold Out'", "Malaysia/Asia Growth Hub"],
    "Truth Delta": ["HIGH", "CRITICAL", "HIGH", "MODERATE"]
})
st.table(discord_df)

st.info("Market Observation: Sunday Feb 8, 2026. The West is regionalizing trade while Asia's industrial engine accelerates. Watch the 'Energy Gating' of AI hubs in Virginia.")
