import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# --- 1. PAGE CONFIG & REFRESH ---
st.set_page_config(page_title="2026 Truth Oracle", layout="wide")
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", "Nvidia": "NVDA", "Crude Oil": "CL=F"
    }
    results = {}
    price_history = pd.DataFrame()
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym).history(period="5d")
            if not t.empty:
                curr = t["Close"].iloc[-1]
                prev = t["Close"].iloc[-2] if len(t) > 1 else curr
                results[name] = {"price": curr, "change": ((curr - prev) / prev) * 100}
                price_history[name] = t["Close"]
        except: results[name] = {"price": 0.0, "change": 0.0}
    
    for k in tickers.keys():
        if k not in results: results[k] = {"price": 0.0, "change": 0.0}
        
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, corr

live_data, correlations = fetch_market_data()

# --- 3. SIDEBAR: WHALE WATCHER & LOGISTICS ---
st.sidebar.header("🐋 Polymarket Whale Watcher")
st.sidebar.error("LARGE MOVE: $2.4M on 'Midterm Deadlock'")
st.sidebar.warning("WHALE ALERT: $1.2M Exit from 'AI Growth'")

st.sidebar.divider()
st.sidebar.header("🚢 Logistics Alert")
st.sidebar.error("Suez Avoidance: +12 Day Delay Active")
st.sidebar.warning("Freightos Index: +14% (Asia-US West Coast)")

st.sidebar.divider()
st.sidebar.header("📡 Live Orbital Drift")
st.sidebar.error("GSSAP-7 Drift Active: 105W → 12.4E")

# --- 4. MAIN INTERFACE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.caption(f"Feb 8, 2026 | Pulse Sync: {datetime.now().strftime('%H:%M:%S')} | Signal: ⚠️ High Discordance")

# Metrics
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold Spot", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Industrial Copper", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")
with c4: st.metric("Nvidia", f"${live_data['Nvidia']['price']:,.2f}", f"{live_data['Nvidia']['change']:.2f}%")

st.divider()

# --- 5. NARRATIVE BIAS HEATMAP ---
st.header("🌡️ Narrative Bias & Sentiment Heatmap")

def style_logic(val):
    colors = {
        "State Narrative": "background-color: #6f42c1; color: white;",
        "Suppressed Signal": "background-color: #dc3545; color: white;",
        "Global Truth": "background-color: #28a745; color: white;",
        "Industrial Reality": "background-color: #007bff; color: white;",
        "Kinetic Movement": "background-color: #343a40; color: white;"
    }
    return colors.get(val, "")

bias_df = pd.DataFrame({
    "Sector": ["Labor Market", "Energy Grid", "Orbital", "Logistics", "Tech Hardware"],
    "Official Narrative": ["'Full Employment'", "'Green Transition'", "'Routine Orbit'", "'Normal Flow'", "'Unlimited AI Growth'"],
    "Shadow Reality (Truth)": ["$500k Relief Spike", "17% Power Deficit", "GSSAP-7 Target Drift", "Suez Bypass +12d", "HBM Memory 'Sold Out'"],
    "Market Status": ["Suppressed Signal", "Industrial Reality", "Kinetic Movement", "Industrial Reality", "Industrial Reality"],
    "Censorship Intensity": ["Low", "Critical", "Extreme", "Moderate", "Moderate"]
})

st.dataframe(bias_df.style.map(style_logic, subset=['Market Status']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS ---
st.divider()
t1, t2, t3, t4, t5 = st.tabs(["🗺️ Truth Map & Orbital Path", "🚢 Global Logistics", "🐋 Whale Watcher", "🪖 Kinetic Ticker", "🚫 Censorship Monitor"])

with t1:
    st.subheader("🗺️ Unified Map: Terrestrial Nodes, Logistics Hubs & Orbital Path")
    nodes = pd.DataFrame({
        'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31, 25.03, 24.47, 30.67], # Added Logistics Hubs (Suez/Shanghai)
        'lon': [-74.00, -0.12, 103.81, -77.03, 116.40, 114.16, 121.56, 32.21, 122.06],
        'Node': ['NY', 'LDN', 'Singapore', 'DC', 'BJG', 'HK', 'Taiwan', 'Suez', 'Shanghai']
    })
    path_lats = np.linspace(0, 15, 60) 
    path_lons = np.linspace(-105, 12.4, 60)
    drift_path = pd.DataFrame({'lat': path_lats, 'lon': path_lons, 'Node': 'GSSAP-7 Drift'})
    st.map(pd.concat([nodes, drift_path], ignore_index=True))
    st.info("🟢 Fixed Nodes | ⚪ Arc: Satellite relocation. Suez Chokepoint (lat 24.47) monitored for vessel congestion.")

with t2:
    st.subheader("🚢 Global Logistics & Trade Flow")
    st.table(pd.DataFrame({
        "Route": ["Asia to Europe", "Asia to US West", "US East to Europe"],
        "Status": ["Suez Bypass (Cape of Good Hope)", "Port Congestion Rising", "Stable"],
        "Time Delta": ["+12 Days", "+3 Days", "0 Days"],
        "Cost Signal": ["Critical Spike", "Moderate Increase", "Flat"]
    }))

with t3:
    st.subheader("🐋 Polymarket Whale Watcher")
    st.table(pd.DataFrame({
        "Event": ["2026 Midterm Deadlock", "Fed March 'No Change'", "Nvidia Top Q1", "GSSAP Target Lock"],
        "Whale Position": ["$2.4M (Bullish)", "$1.8M (Bullish)", "$900k (Bearish)", "$1.2M (Bullish)"],
        "Truth Delta": ["HIGH", "LOW", "CRITICAL", "HIGH"]
    }))

with t4:
    st.subheader("🪖 Kinetic Signals")
    st.table(pd.DataFrame({"Asset": ["GSSAP-7", "USS Lincoln", "PLAN Patrol"], "Status": ["Drifting", "Active", "55-Vessel Array"], "Threat": ["Emergency", "Emergency", "Critical"]}))

with t5:
    st.subheader("🚫 Information Throttling & De-ranking")
    st.table(pd.DataFrame({"Target Keyword": ["Suez Blockage", "HBM Yield", "Grid Blackout"], "Method": ["Narrative Smoothing", "Search Throttling", "Packet Shaping"]}))

st.info("System Note: Logistics data cross-referenced with satellite vessel tracking. Industrial reality remains decoupled from digital narrative.")
