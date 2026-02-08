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
    tickers = {"S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD", "Copper": "HG=F"}
    results = {}
    price_history = pd.DataFrame()
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym).history(period="30d")
            results[name] = {"price": t["Close"].iloc[-1], "change": ((t["Close"].iloc[-1] - t["Open"].iloc[-1]) / t["Open"].iloc[-1]) * 100}
            price_history[name] = t["Close"]
        except: results[name] = {"price": 0.0, "change": 0.0}
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, corr

live_data, correlations = fetch_market_data()

# --- 3. SIDEBAR: ORBITAL & CENSORSHIP ---
st.sidebar.header("👁️ Information Integrity")
censorship_level = 64 
st.sidebar.progress(censorship_level, text=f"Shadow-Ban Intensity: {censorship_level}%")
st.sidebar.warning("ALERT: Search throttling on 'GSSAP Maneuvers' detected.")

st.sidebar.divider()
st.sidebar.header("📡 Orbital Drift Alert")
st.sidebar.error("CRITICAL: 2 Adversary Inspector Satellites relocated to GEO Slots 12.4E and 105W.")

# --- 4. MAIN INTERFACE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Breaking:** 🪖 USSF-87 mission launched Feb 12; two GSSAP satellites entering GEO to track 'Shadow' maneuvers.")

# Metrics Row
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500 (Domestic)", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold (Truth Signal)", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Bitcoin (Exit Asset)", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c4: st.metric("Copper (Industrial)", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

st.divider()

# --- 5. NARRATIVE BIAS HEATMAP ---
st.header("🌡️ Narrative Bias & Information Suppression")
def style_logic(val):
    colors = {"State Narrative": "background-color: #6f42c1; color: white;", "Suppressed Signal": "background-color: #dc3545; color: white;", 
              "Global Truth": "background-color: #28a745; color: white;", "Kinetic Ready": "background-color: #343a40; color: white;"}
    return colors.get(val, "")

bias_df = pd.DataFrame({
    "Sector": ["Labor Market", "Energy Grid", "Orbital", "Military", "AI Scaling"],
    "Official Narrative": ["'Full Employment'", "'Green Transition'", "'Routine Launch'", "'Peaceful Patrol'", "'Unlimited Growth'"],
    "Shadow Signal (Truth)": ["$500k Layoff Relief", "17% Power Deficit", "Maneuverable GEO Drift", "South China Sea Blockade", "HBM4 Sold Out"],
    "Market Status": ["State Narrative", "Suppressed Signal", "Kinetic Ready", "Kinetic Ready", "Suppressed Signal"]
})
st.dataframe(bias_df.style.map(style_logic, subset=['Market Status']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS: GEOPOLITICAL TRUTH MAP ---
st.divider()
t1, t2, t3, t4 = st.tabs(["🗺️ Geopolitical Truth Map", "🪖 Military & Orbital Tickers", "📊 Correlation", "🆘 Social Relief"])

with t1:
    st.subheader("🗺️ Unified Truth Map: Terrestrial Nodes & Orbital Slots")
    # Coordinates for Truth Nodes and Satellite Ground-Tracks/Slots
    map_data = pd.DataFrame({
        'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31, 25.03, -15.0, 45.0], # Added Orbital Slots as pseudo-coords
        'lon': [-74.00, -0.12, 103.81, -77.03, 116.40, 114.16, 121.56, 12.4, -105.0],
        'Type': ['Node', 'Node', 'Node', 'Control', 'Control', 'Node', 'Kinetic', 'Orbital Drift', 'Orbital Drift']
    })
    st.map(map_data)
    st.info("🟢 Nodes: Uncensored data. | 🔴 Control: Narrative steering. | 🪖 Orbital Drift: Strategic satellite repositioning.")

with t2:
    st.subheader("🪖 Kinetic Ticker: Ground & Orbit")
    mil_move = pd.DataFrame({
        "Asset": ["GSSAP 7/8", "Steadfast Dart 2026", "Yaogan Constellation", "USS Lincoln"],
        "Status": ["GEO Deployment (Live)", "NATO Non-US Exercise", "Indo-Pacific Phasing", "Active Strike Stance"],
        "Signal": ["Counterspace Readiness", "Allied Fracture", "Carrier Target Tracking", "Regional War Risk"],
        "Alert": ["Extreme", "Elevated", "Critical", "Emergency"]
    })
    st.table(mil_move)

with t3:
    st.subheader("Asset Correlation")
    if not correlations.empty: st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

st.info("Market Observation: Narrative control has shifted from 'Deletion' to 'Latency.' The satellite relocations are the only 'Hard Clock' remaining for conflict timing.")
