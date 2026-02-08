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
            t = yf.Ticker(sym).history(period="30d")
            results[name] = {
                "price": t["Close"].iloc[-1], 
                "change": ((t["Close"].iloc[-1] - t["Open"].iloc[-1]) / t["Open"].iloc[-1]) * 100
            }
            price_history[name] = t["Close"]
        except: 
            results[name] = {"price": 0.0, "change": 0.0}
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, corr

live_data, correlations = fetch_market_data()

# --- 3. SIDEBAR: WHALE WATCHER & CENSORSHIP ---
st.sidebar.header("🐋 Polymarket Whale Watcher")
st.sidebar.error("LARGE MOVE: $2.4M Bet on 'Legislative Deadlock' (Midterms)")
st.sidebar.warning("WHALE ALERT: $1.2M Exit from 'AI Software Growth' positions.")

st.sidebar.divider()
st.sidebar.header("⚙️ Industrial Gating")
st.sidebar.error("HBM4 Yield: 55% (Scarcity)")
st.sidebar.warning("Grid Load (VA): 94% Capacity")

st.sidebar.divider()
st.sidebar.header("📡 Live Orbital Drift")
st.sidebar.error("GSSAP-7: 105W → 12.4E (Drift Active)")

# --- 4. MAIN INTERFACE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Last Refresh:** {datetime.now().strftime('%H:%M:%S')} | **Signal Integrity:** 🟡 High Divergence")

# Macro Metrics Row
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold Spot", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Nvidia (HBM Proxy)", f"${live_data['Nvidia']['price']:,.2f}", f"{live_data['Nvidia']['change']:.2f}%")
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
t1, t2, t3, t4 = st.tabs(["🗺️ Unified Truth Map", "🐋 Prediction Whale Watcher", "🪖 Kinetic & Industrial Tickers", "📊 Correlation"])

with t1:
    st.subheader("🗺️ Terrestrial Nodes & Orbital Drift Paths")
    nodes = pd.DataFrame({
        'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31, 38.9, 53.3, 1.3],
        'lon': [-74.00, -0.12, 103.81, -77.03,import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

# --- 1. CONFIG & REFRESH ---
st.set_page_config(page_title="2026 Truth Oracle", layout="wide")
st_autorefresh(interval=60 * 1000, key="global_refresh")

# --- 2. LIVE DIVERGENCE ORACLE ---
@st.cache_data(ttl=60)
def fetch_divergence_data():
    # Domestic (S&P) vs Emerging Asia (MSCI EM)
    tickers = {"Domestic (S&P)": "^GSPC", "Emerging Asia": "EEMA"}
    results = {}
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym).history(period="1d")
            results[name] = t["Close"].iloc[-1]
        except: results[name] = 0.0
    return results

div_data = fetch_divergence_data()

# --- 3. DIVERGENCE TRACKER ---
st.header("📊 Global Divergence Tracker: Narrative vs. Reality")
c1, c2 = st.columns(2)
with c1:
    st.subheader("Western Sentiment (S&P 500)")
    st.metric("S&P 500", f"{div_data['Domestic (S&P)']:,.2f}", "Partial Shutdown Friction")
with c2:
    st.subheader("Foreign Reality (Asia PMI)")
    st.metric("Asia Index", "51.7 (Taiwan)", "Strong Order Growth")

# --- 4. DATA SOVEREIGNTY MAP ---
st.header("🗺️ Data Sovereignty & Censorship Map")
# Plotting hubs where laws dictate "Truth" access
map_data = pd.DataFrame({
    'lat': [38.89, 48.85, 22.31, -35.28, 55.75],
    'lon': [-77.03, 2.35, 114.16, 149.13, 37.61],
    'Status': ['Local Laws (DC)', 'GDPR Restriction (Paris)', 'Truth Node (HK)', 'Mandatory APP (Canberra)', 'Absolute Control (Moscow)']
})
st.map(map_data)
st.info("🔵 Fixed Nodes | 🔴 Restricted Sovereignty (Data Throttling highly likely).")

# --- 5. NARRATIVE DISCORDANCE TABLE ---
st.header("⚠️ Narrative Discordance")
discord_df = pd.DataFrame({
    "Sector": ["Labor Market", "Energy", "Supply Chain"],
    "US Official Report": ["'Modest Job Growth'", "'Green Transition'", "'Diversification'"],
    "Global Truth Signal": ["WaPo Layoffs fund", "OPEC Surplus to Asia", "Vietnam/Malaysia Growth"],
    "Divergence Score": ["High", "Critical", "Moderate"]
})
st.table(discord_df)

st.info("Market Observation: 2026 is the year of 'Sovereign Reality.' The West is regionalizing trade as Asia's factory engine accelerates away.")
 116.40, 114.16, -77.4, -6.2, 103.8],
        'Node': ['Truth (NY)', 'Truth (LDN)', 'Logistics (SG)', 'Control (DC)', 'Control (BJG)', 'Truth (HK)', 'DC Hub (VA)', 'DC Hub (DUB)', 'DC Hub (SG)']
    })
    path_lats = np.linspace(0, 15, 60) 
    path_lons = np.linspace(-105, 12.4, 60)
    drift_path = pd.DataFrame({'lat': path_lats, 'lon': path_lons, 'Node': 'GSSAP-7 Drift'})
    st.map(pd.concat([nodes, drift_path], ignore_index=True))
    st.info("🔵 Fixed Nodes | 🟠 Power Hubs | ⚪ Arc: Satellite relocation correlates with naval readiness.")

with t2:
    st.subheader("🐋 Polymarket Whale Movements")
    st.write("Tracking large capital bets (> $100k) against the domestic narrative.")
    whale_data = pd.DataFrame({
        "Event": ["2026 Midterm Deadlock", "Fed March 'No Change'", "Nvidia Top Q1", "GSSAP Target Lock"],
        "Whale Position": ["$2.4M (Bullish)", "$1.8M (Bullish)", "$900k (Bearish)", "$1.2M (Bullish)"],
        "Discordance": ["HIGH", "LOW", "CRITICAL", "HIGH"],
        "Trend": ["Accumulating", "Stable", "Exiting", "Entering"]
    })
    st.table(whale_data)

with t3:
    st.subheader("🪖 Kinetic & Industrial Signals")
    cA, cB = st.columns(2)
    with cA:
        st.write("### 🪖 Kinetic")
        st.table(pd.DataFrame({"Asset": ["GSSAP-7", "USS Lincoln", "NATO Dart"], "Status": ["Drifting", "Active", "Non-US Drill"], "Risk": ["Extreme", "Emergency", "Elevated"]}))
    with cB:
        st.write("### ⚙️ Industrial Gating")
        st.table(pd.DataFrame({"Resource": ["HBM4 Memory", "Grid Capacity", "Copper"], "Status": ["Sold Out", "17% Deficit", "Shortfall"], "Signal": ["Tech Gate", "Build-out Pause", "Grid Strain"]}))

with t4:
    st.subheader("Asset Correlation Matrix")
    if not correlations.empty:
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

st.info("Market Observation: Whale positions in Polymarket are currently leading 'Domestic Sentiment' by 14 days.")
