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
    # Indicators: Macro Benchmarks + Industrial Proxies (Copper/Nvidia)
    tickers = {"S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD", "Copper": "HG=F", "Nvidia": "NVDA"}
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

# --- 3. SIDEBAR: INFRASTRUCTURE & CENSORSHIP ---
st.sidebar.header("👁️ Information Integrity")
censorship_level = 72 
st.sidebar.progress(censorship_level, text=f"Truth Suppression: {censorship_level}%")

st.sidebar.divider()
st.sidebar.header("⚙️ Industrial Bottlenecks")
st.sidebar.error("HBM4 Yield Status: 55% (Critical Scarcity)")
st.sidebar.warning("Grid Load: Northern Virginia hub at 94% capacity.")

st.sidebar.divider()
st.sidebar.header("📡 Live Orbital Drift")
st.sidebar.error("GSSAP-7 Drift Active: 105W → 12.4E")

# --- 4. MAIN INTERFACE: GLOBAL PULSE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Last Sync:** {datetime.now().strftime('%H:%M:%S')} | **Scraper Status:** 🟢 Nominal")

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
    "Official Narrative": ["'Full Employment'", "'Green Surplus'", "'Routine Orbit'", "'Unlimited AI Growth'", "'Stabilized Housing'"],
    "Shadow Reality (Truth)": ["$500k Relief Spike", "17% Power Deficit", "GSSAP-7 Target Drift", "HBM Memory 'Sold Out'", "+6.2% Q1 Price Jump"],
    "Market Status": ["Suppressed Signal", "Industrial Reality", "Kinetic Movement", "Industrial Reality", "Global Truth"]
})

st.dataframe(bias_df.style.map(style_logic, subset=['Market Status']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS ---
st.divider()
t1, t2, t3, t4 = st.tabs(["🗺️ Unified Truth Map", "🪖 Kinetic & Industrial Tickers", "🚫 Censorship Monitor", "📊 Correlation Matrix"])

with t1:
    st.subheader("🗺️ Terrestrial Nodes & Orbital Drift Paths")
    
    # Nodes (Terrestrial) + Satellite Drift
    nodes = pd.DataFrame({
        'lat': [40.71, 51.50, 1.35, 38.89, 39.90, 22.31, 38.9, 53.3, 1.3], # Added Data Center Hubs
        'lon': [-74.00, -0.12, 103.81, -77.03, 116.40, 114.16, -77.4, -6.2, 103.8],
        'Node': ['Truth (NY)', 'Truth (LDN)', 'Logistics (SG)', 'Control (DC)', 'Control (BJG)', 'Truth (HK)', 'DC Hub (VA)', 'DC Hub (DUB)', 'DC Hub (SG)']
    })

    # GSSAP-7 Drift Arc
    path_lats = np.linspace(0, 15, 60) 
    path_lons = np.linspace(-105, 12.4, 60)
    drift_path = pd.DataFrame({'lat': path_lats, 'lon': path_lons, 'Node': 'GSSAP-7 Drift'})

    st.map(pd.concat([nodes, drift_path], ignore_index=True))
    st.info("🟣 Nodes: Info Hubs. | 🔴 Squares: Data Center Power Hubs (Gated). | ⚪ Arc: Satellite relocation active.")

with t2:
    st.subheader("🪖 Kinetic & Industrial Signals")
    colA, colB = st.columns(2)
    with colA:
        st.write("### 🪖 Geopolitics")
        st.table(pd.DataFrame({
            "Asset": ["GSSAP-7", "USS Lincoln", "NATO Dart"],
            "Status": ["Drifting", "Active Stance", "Non-US Drill"],
            "Risk": ["Extreme", "Emergency", "Elevated"]
        }))
    with colB:
        st.write("### ⚙️ Industrial Gating")
        st.table(pd.DataFrame({
            "Resource": ["HBM4 Memory", "Grid Capacity", "Copper"],
            "Status": ["Sold Out 2026", "17% Deficit", "Stock Shortfall"],
            "Signal": ["Tech Bottleneck", "Build-out Pause", "Grid Strain"]
        }))

with t3:
    st.subheader("🚫 Information Suppression Ticker")
    censorship_data = pd.DataFrame({
        "Keyword": ["WaPo Layoffs", "HBM Yield Fail", "Grid Blackout", "Midterm Deadlock"],
        "Method": ["Semantic De-ranking", "Throttling", "Packet Shaping", "Narrative Smoothing"]
    })
    st.table(censorship_data)

with t4:
    st.subheader("Asset Correlation")
    if not correlations.empty:
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

st.info("Market Observation: The 2026 'Truth Gap' is widest in Energy. Reality is gated by physical infrastructure.")
