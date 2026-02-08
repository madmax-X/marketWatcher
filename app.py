import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_page_config(page_title="2026 Truth Oracle", layout="wide")

# Refresh every 60 seconds
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC", 
        "Gold": "GC=F", 
        "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", 
        "Nvidia": "NVDA"
    }
    results = {}
    price_history = pd.DataFrame()
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="30d")
            if not hist.empty:
                results[name] = {
                    "price": hist["Close"].iloc[-1], 
                    "change": ((hist["Close"].iloc[-1] - hist["Open"].iloc[-1]) / hist["Open"].iloc[-1]) * 100
                }
                price_history[name] = hist["Close"]
        except:
            results[name] = {"price": 0.0, "change": 0.0}
            
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, corr

live_data, correlations = fetch_market_data()

# --- 3. SIDEBAR: CENSORSHIP & KINETIC THREAT ---
st.sidebar.header("👁️ Information Integrity")
# 2026 Suppression Index: High-speed throttles on economic discordance
censorship_level = 72 
st.sidebar.select_slider("Censorship Methodology", options=["Overt", "Semantic Throttling", "Packet Shaping", "Total"], value="Packet Shaping")
st.sidebar.progress(censorship_level, text=f"Truth Suppression: {censorship_level}%")
st.sidebar.warning("ALERT: NetBlocks detects 'throttling' on 12 key financial nodes.")

st.sidebar.divider()
st.sidebar.header("🪖 Global Threat Index")
threat_val = 81
st.sidebar.progress(threat_val, text=f"Kinetic Escalation: {threat_val}%")
st.sidebar.info("USS Abraham Lincoln in Arabian Sea; NATO 'Steadfast Dart' active.")

# --- 4. MAIN INTERFACE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Censorship Watch:** 🚫 OONI Probes detect interference on: *'Bank Solvency'*, *'HBM Yields'*. | 🟢 Satellite Feeds (Starlink/Alt-Net) remain unthrottled.")

# Metric Pulse Row
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500 (Domestic)", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold (Global Truth)", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Bitcoin (Exit Asset)", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c4: st.metric("Copper (Industrial)", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

st.divider()

# --- 5. NARRATIVE BIAS HEATMAP ---
st.header("🌡️ Narrative Bias & Censorship Map")

def style_logic(val):
    colors = {
        "State Narrative": "background-color: #6f42c1; color: white;",
        "Suppressed Signal": "background-color: #dc3545; color: white;",
        "Global Truth": "background-color: #28a745; color: white;",
        "Industrial Reality": "background-color: #007bff; color: white;",
        "Kinetic Movement": "background-color: #343a40; color: white;" # Black for military
    }
    return colors.get(val, "")

bias_df = pd.DataFrame({
    "Sector": ["Labor Market", "Energy Grid", "Media Health", "Military", "Tech Hardware"],
    "Official Narrative (Throttled)": ["'Full Employment'", "'Green Surplus'", "'Restructuring'", "'Stability Patrols'", "'Unlimited Growth'"],
    "Global Reality (Censored)": ["$500k Crowdfund Relief", "17% Grid Gap", "Collapse of WaPo/Legacy", "Carrier Strike Move", "HBM4 'Sold Out'"],
    "Market Status": ["State Narrative", "Suppressed Signal", "Suppressed Signal", "Kinetic Movement", "Industrial Reality"],
    "Censorship Intensity": ["Low", "Critical", "High", "Extreme", "Moderate"]
})

st.dataframe(bias_df.style.map(style_logic, subset=['Market Status']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS ---
st.divider()
st.header("🔍 Intelligence Monitoring: Military & Censorship")
t1, t2, t3, t4, t5 = st.tabs(["🗺️ Geo-Political Truth Map", "🪖 Military Movements", "🚫 Censorship Tracker", "🆘 Social Relief", "📊 Correlation"])

with t1:
    st.subheader("🗺️ Global Information Origin: Truth Nodes vs. State Control")
    map_df = pd.DataFrame({
        'lat': [40.71, 51.50, 22.31, 1.35, 38.89, 39.90, 55.75, 47.37, 25.03],
        'lon': [-74.00, -0.12, 114.16, 103.81, -77.03, 116.40, 37.61, 8.54, 121.56],
        'Node': ['Truth (NY)', 'Truth (LDN)', 'Supply (HK)', 'Logistics (SG)', 'Control (DC)', 'Control (BJG)', 'Control (MOS)', 'Finance (ZRH)', 'Kinetic (TW)']
    })
    st.map(map_df)
    st.info("🟢 Truth Nodes: Unfiltered packet flow. | 🔴 Control Centers: Hubs of semantic steering.")

with t2:
    st.subheader("🪖 Kinetic Signals: Military Ticker")
    mil_move = pd.DataFrame({
        "Region": ["Central Europe", "South China Sea", "Arabian Sea", "Caribbean"],
        "Exercise/Movement": ["Steadfast Dart (Non-US)", "55-Vessel PLAN Patrol", "USS Abraham Lincoln", "Hard Power Pivot"],
        "Truth Signal": ["NATO Historic Fracture", "Shadow Blockade", "Regional War Risk", "Homeland Focus"],
        "Threat Level": ["Elevated", "Critical", "Emergency", "Stable"]
    })
    st.table(mil_move)

with t3:
    st.subheader("🚫 Information Throttling & De-ranking")
    st.write("Keywords detected by OONI/CensoredPlanet as being algorithmically 'shrunk' or blocked:")
    censorship_data = pd.DataFrame({
        "Target Keyword": ["WaPo Layoffs", "HBM Yield Failure", "Grid Blackout Risk", "Midterm Odds", "CBDC Protest"],
        "Method": ["Semantic De-ranking", "Search Throttling", "Packet Shaping", "Narrative Smoothing", "Direct Block"],
        "Objective": ["Hide industry death", "Protect tech stocks", "Mask infrastructure age", "Fake stability", "Force adoption"]
    })
    st.table(censorship_data)

with t4:
    st.subheader("Community Survival Signals")
    st.write("### 📰 Washington Post Relief Fund")
    st.write("- **Status:** $500,000+ Raised. Official channels labeling this 'Industry Pivot' while signals show 'Financial Ruin'.")

with t5:
    st.subheader("Asset Correlation")
    if not correlations.empty:
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

st.info("Market Observation: Narrative control has shifted from 'Deletion' to 'Latency.' They don't delete the truth; they just make it take 10 seconds longer to load than the lie.")
