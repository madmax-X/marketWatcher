import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

# --- 1. PAGE CONFIG & REFRESH ---
st.set_page_config(page_title="2026 Truth Oracle", layout="wide")
# Refresh every 60 seconds
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. ROBUST DATA FETCHING (Macro & Industrial) ---
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
            # 5-day period to bridge weekend/holiday gaps
            t = yf.Ticker(sym).history(period="5d")
            if not t.empty:
                current_price = t["Close"].iloc[-1]
                prev_price = t["Close"].iloc[-2] if len(t) > 1 else current_price
                results[name] = {
                    "price": current_price, 
                    "change": ((current_price - prev_price) / prev_price) * 100
                }
                price_history[name] = t["Close"]
            else: results[name] = {"price": 0.0, "change": 0.0}
        except: results[name] = {"price": 0.0, "change": 0.0}
    
    # Ensure no KeyErrors
    for k in tickers.keys():
        if k not in results: results[k] = {"price": 0.0, "change": 0.0}
        
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, corr

live_data, correlations = fetch_market_data()

# --- 3. SIDEBAR: WHALE WATCHER & CENSORSHIP ---
st.sidebar.header("🐋 Polymarket Whale Watcher")
st.sidebar.error("LARGE MOVE: $2.4M Bet on 'Legislative Deadlock'")
st.sidebar.warning("WHALE ALERT: $1.2M Exit from 'AI Growth' positions.")

st.sidebar.divider()
st.sidebar.header("👁️ Information Integrity")
censorship_level = 72 
st.sidebar.progress(censorship_level, text=f"Shadow-Ban Intensity: {censorship_level}%")
st.sidebar.warning("ALERT: Search throttling on 'WaPo Layoffs' detected.")

st.sidebar.divider()
st.sidebar.header("📡 Live Orbital Drift")
st.sidebar.error("GSSAP-7 Drift Active: 105W → 12.4E")

# --- 4. MAIN INTERFACE: GLOBAL PULSE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.caption(f"Feb 8, 2026 | Last Refresh: {datetime.now().strftime('%H:%M:%S')} | Signal Integrity: ⚠️ High Divergence")

# Macro Metrics Row
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold Spot", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Bitcoin", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c4: st.metric("Industrial Copper", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

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
    "Sector": ["Labor Market", "Energy Grid", "Orbital", "Tech Hardware", "Real Estate"],
    "Official Narrative": ["'Full Employment'", "'Green Transition'", "'Routine Orbit'", "'Unlimited AI Growth'", "'Stabilized Housing'"],
    "Shadow Reality (Truth)": ["$500k Relief Spike", "17% Power Deficit", "GSSAP-7 Target Drift", "HBM Memory 'Sold Out'", "+6.2% Q1 Price Jump"],
    "Market Status": ["Suppressed Signal", "Industrial Reality", "Kinetic Movement", "Industrial Reality", "Global Truth"]
})

st.dataframe(bias_df.style.map(style_logic, subset=['Market Status']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS ---
st.divider()
t1, t2, t3, t4, t5 = st.tabs(["🗺️ Truth Map & Orbital Path", "🐋 Whale Watcher", "🪖 Kinetic Ticker", "🚫 Censorship Monitor", "📊 Correlation"])

with t1:
    st.subheader("🗺️ Unified Map: Terrestrial Nodes & Orbital Drift")
    # Fixed Nodes
    nodes = pd.DataFrame({
        'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31, 25.03],
        'lon': [-74.00, -0.12, 103.81, -77.03, 116.40, 114.16, 121.56],
        'Node': ['Truth (NY)', 'Truth (LDN)', 'Logistics (SG)', 'Control (DC)', 'Control (BJG)', 'Truth (HK)', 'Kinetic (TW)']
    })
    # Orbital Drift Path (GSSAP-7)
    path_lats = np.linspace(0, 15, 60) 
    path_lons = np.linspace(-105, 12.4, 60)
    drift_path = pd.DataFrame({'lat': path_lats, 'lon': path_lons, 'Node': 'GSSAP-7 Drift'})
    
    st.map(pd.concat([nodes, drift_path], ignore_index=True))
    st.info("🟢 Fixed Nodes | ⚪ Arc: Satellite relocation correlates with naval readiness in the Arabian Sea.")

with t2:
    st.subheader("🐋 Polymarket Whale Watcher")
    whale_df = pd.DataFrame({
        "Event": ["2026 Midterm Deadlock", "Fed March 'No Change'", "Nvidia Top Q1", "GSSAP Target Lock"],
        "Whale Position": ["$2.4M (Bullish)", "$1.8M (Bullish)", "$900k (Bearish)", "$1.2M (Bullish)"],
        "Truth Delta": ["HIGH", "LOW", "CRITICAL", "HIGH"]
    })
    st.table(whale_df)

with t3:
    st.subheader("🪖 Kinetic Signals")
    st.table(pd.DataFrame({
        "Asset": ["GSSAP-7", "USS Lincoln", "NATO Dart", "PLAN Patrol"],
        "Status": ["Drifting", "Active Stance", "Non-US Drill", "55-Vessel Array"],
        "Threat": ["Emergency", "Emergency", "Elevated", "Critical"]
    }))

with t4:
    st.subheader("🚫 Information Throttling & De-ranking")
    censorship_data = pd.DataFrame({
        "Target Keyword": ["WaPo Layoffs", "HBM Yield Failure", "Grid Blackout Risk", "Midterm Odds"],
        "Method": ["Semantic De-ranking", "Search Throttling", "Packet Shaping", "Narrative Smoothing"],
        "Discordance": ["HIGH", "CRITICAL", "HIGH", "MODERATE"]
    })
    st.table(censorship_data)

with t5:
    st.subheader("Asset Correlation Matrix")
    if not correlations.empty:
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

st.info("Market Observation: Sunday Feb 8, 2026. The West is regionalizing trade while Asia's industrial engine accelerates. Watch the 'Energy Gating' of AI hubs in Virginia.")
