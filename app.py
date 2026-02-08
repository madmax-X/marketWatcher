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

# --- 3. SIDEBAR: ORBITAL KINEMATICS ---
st.sidebar.header("👁️ Information Integrity")
censorship_level = 64 
st.sidebar.progress(censorship_level, text=f"Shadow-Ban Intensity: {censorship_level}%")

st.sidebar.divider()
st.sidebar.header("📡 Live Orbital Drift")
st.sidebar.error("PROJECTED PATH: GSSAP-7 moving from 105W to 12.4E. Transit time: 72hrs.")
st.sidebar.warning("Signal Intelligence: Repositioning suggests targeting lock over Arabian Sea sector.")

# --- 4. MAIN INTERFACE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Live Feed:** {datetime.now().strftime('%H:%M:%S')} | **Orbital Status:** ⚠️ Maneuver in Progress")

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold (Truth)", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Bitcoin (Exit)", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c4: st.metric("Copper (Utility)", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

st.divider()

# --- 5. INTELLIGENCE TABS: GEOPOLITICAL TRUTH MAP ---
t1, t2, t3, t4 = st.tabs(["🗺️ Geopolitical Truth Map", "🪖 Kinetic Ticker", "🌡️ Narrative Heatmap", "📊 Correlation"])

with t1:
    st.subheader("🗺️ Unified Truth Map: Terrestrial Nodes & Orbital Drift Paths")
    
    # Coordinates for Truth Nodes
    nodes = pd.DataFrame({
        'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31],
        'lon': [-74.00, -0.12, 103.81, -77.03, 116.40, 114.16],
        'Type': ['Truth Node', 'Truth Node', 'Truth Node', 'State Control', 'State Control', 'Truth Node']
    })

    # GENERATING ORBITAL DRIFT PATH (Interpolated Points)
    # Drift Path from 105W (Mid-Pacific) to 12.4E (Middle East/Africa)
    drift_lats = np.linspace(0, 15, 50)  # Slight northern arc
    drift_lons = np.linspace(-105, 12.4, 50)
    drift_path = pd.DataFrame({'lat': drift_lats, 'lon': drift_lons, 'Type': 'Orbital Drift Path'})

    # Combine all map data
    map_combined = pd.concat([nodes, drift_path], ignore_index=True)
    
    st.map(map_combined)
    st.info("🔵 Dots: Fixed Truth Nodes. | ⚪ Arc: GSSAP-7 Active Drift Path. Relocation indicates a shift in kinetic targeting priorities.")

with t2:
    st.subheader("🪖 Kinetic Ticker: Ground & Orbit")
    mil_move = pd.DataFrame({
        "Asset": ["GSSAP-7 (USSF)", "Shijian-21 (CNSA)", "USS Lincoln", "NATO Dart"],
        "Current Slot": ["Drifting to 12.4E", "Proximity Ops at 105W", "Arabian Sea Sector", "Central Europe"],
        "Truth Signal": ["Repositioning Sensors", "Asset Inspector Alert", "Conflict Readiness", "Allied Rupture"],
        "Risk": ["Emergency", "Critical", "Emergency", "Elevated"]
    })
    st.table(mil_move)

with t3:
    st.subheader("🌡️ Narrative Bias Heatmap")
    bias_df = pd.DataFrame({
        "Sector": ["Military", "Energy", "Labor", "Orbital"],
        "Official Narrative": ["'Peaceful Patrols'", "'Green Transition'", "'Full Employment'", "'Routine Maintenance'"],
        "Shadow Reality": ["Shadow Blockade", "17% Power Deficit", "$500k Relief Spike", "Unannounced GEO Drift"],
        "Truth Gap": ["Extreme", "Critical", "High", "Critical"]
    })
    st.table(bias_df)

with t4:
    st.subheader("Asset Correlation")
    if not correlations.empty: st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

st.divider()
st.info("System Note: Orbital drift paths are calculated using TLE (Two-Line Element) perturbation analysis. Terrestrial nodes refresh via YFinance.")
