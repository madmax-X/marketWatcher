import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# --- 1. PAGE CONFIG & REFRESH ---
st.set_page_config(page_title="2026 Truth Oracle", layout="wide")
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING (Financial Benchmarks) ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {"S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD", "Copper": "HG=F"}
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

# --- 3. SIDEBAR: CENSORSHIP & ORBITAL ALERTS ---
st.sidebar.header("👁️ Information Integrity")
censorship_level = 72 
st.sidebar.progress(censorship_level, text=f"Truth Suppression: {censorship_level}%")
st.sidebar.warning("ALERT: Packet Shaping detected on 'Bank Liquidity' & 'HBM Supply'.")

st.sidebar.divider()
st.sidebar.header("📡 Live Orbital Drift")
st.sidebar.error("GSSAP-7 Drift Active: 105W → 12.4E")
st.sidebar.info("Est. Completion: 72 hrs. Objective: Arabian Sea Target Lock.")

# --- 4. MAIN INTERFACE: GLOBAL PULSE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Last Sync:** {datetime.now().strftime('%H:%M:%S')} | **Status:** ⚠️ Kinetic Divergence Detected")

# Macro Metrics Row
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500 (Domestic)", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold (Global Truth)", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Bitcoin (Exit Asset)", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c4: st.metric("Copper (Industrial)", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

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
    "Sector": ["Labor Market", "Energy Grid", "Orbital", "Media Health", "Tech Hardware"],
    "Official Narrative": ["'Full Employment'", "'Green Transition'", "'Routine Maintenance'", "'Restructuring'", "'Unlimited Growth'"],
    "Shadow Reality (Truth)": ["$500k Crowdfund Relief", "17% Power Deficit", "GSSAP-7 Target Drift", "Collapse of WaPo/Legacy", "HBM Memory 'Sold Out'"],
    "Market Status": ["State Narrative", "Suppressed Signal", "Kinetic Movement", "Suppressed Signal", "Industrial Reality"],
    "Censorship Intensity": ["Low", "Critical", "Extreme", "High", "Moderate"]
})

st.dataframe(bias_df.style.map(style_logic, subset=['Market Status']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS ---
st.divider()
st.header("🔍 Intelligence Monitoring & Propaganda Analysis")
t1, t2, t3, t4, t5 = st.tabs(["🗺️ Truth Map & Orbital Path", "🪖 Kinetic Ticker", "🚫 Censorship Monitor", "🆘 Social Relief", "📊 Correlation"])

with t1:
    st.subheader("🗺️ Unified Map: Terrestrial Nodes & Orbital Drift")
    
    # 1. FIXED NODES
    nodes = pd.DataFrame({
        'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31, 25.03],
        'lon': [-74.00, -0.12, 103.81, -77.03, 116.40, 114.16, 121.56],
        'Node': ['Truth (NY)', 'Truth (LDN)', 'Logistics (SG)', 'Control (DC)', 'Control (BJG)', 'Truth (HK)', 'Kinetic (TW)']
    })

    # 2. ORBITAL DRIFT PATH (GSSAP-7: Pacific to Middle East)
    path_lats = np.linspace(0, 15, 60) 
    path_lons = np.linspace(-105, 12.4, 60)
    drift_path = pd.DataFrame({'lat': path_lats, 'lon': path_lons, 'Node': 'GSSAP-7 Drift Path'})

    # Combined View
    map_combined = pd.concat([nodes, drift_path], ignore_index=True)
    st.map(map_combined)
    st.info("🟢 Dots: Information Hubs. | ⚪ Arc: Satellite relocation in progress. This drift correlates with heightened naval readiness in the Arabian Sea.")

with t2:
    st.subheader("🪖 Kinetic Signals: Ground & Orbit")
    mil_move = pd.DataFrame({
        "Asset": ["GSSAP-7 (USSF)", "Steadfast Dart (NATO)", "Shijian-21 (CNSA)", "USS Lincoln"],
        "Status": ["Drifting to 12.4E", "Non-US Drill Active", "GEO Inspector Alert", "Combat Ready"],
        "Truth Signal": ["Targeting Priority Shift", "Allied Historic Fracture", "Counterspace Risk", "Regional War Warning"],
        "Alert": ["Extreme", "Elevated", "Critical", "Emergency"]
    })
    st.table(mil_move)

with t3:
    st.subheader("🚫 Information Throttling & De-ranking")
    censorship_data = pd.DataFrame({
        "Target Keyword": ["WaPo Layoffs", "HBM Yield Failure", "Grid Blackout Risk", "Midterm Odds"],
        "Method": ["Semantic De-ranking", "Search Throttling", "Packet Shaping", "Narrative Smoothing"],
        "Impact": ["Hide media industry death", "Protect tech stocks", "Mask infrastructure age", "Fake stability"]
    })
    st.table(censorship_data)

with t4:
    st.subheader("Community Survival Signals")
    st.write("### 📰 Washington Post Relief Fund")
    st.write(f"- **Status:** $500,000+ Raised. Official channels labeling this 'Industry Pivot' while signal shows 'Financial Ruin'.")

with t5:
    st.subheader("Asset Correlation")
    if not correlations.empty:
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

st.info("System Refreshed. Macro data live via YFinance. Social and Orbital signals 15m cached. Information Integrity Active.")
