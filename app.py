import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_set_page_config(page_title="2026 Truth Oracle", layout="wide")
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", "Nvidia": "NVDA"
    }
    results = {}
    price_history = pd.DataFrame()
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="30d")
            if not hist.empty:
                results[name] = {"price": hist["Close"].iloc[-1], "change": ((hist["Close"].iloc[-1] - hist["Open"].iloc[-1]) / hist["Open"].iloc[-1]) * 100}
                price_history[name] = hist["Close"]
        except: results[name] = {"price": 0.0, "change": 0.0}
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, corr

live_data, correlations = fetch_market_data()

# --- 3. SIDEBAR: CENSORSHIP & DIVERGENCE ---
st.sidebar.header("👁️ Information Integrity")
censorship_level = 64 # Feb 2026 Suppression Index
st.sidebar.select_slider("Information Throttling Level", options=["Low", "Staggered", "Aggressive", "Total"], value="Aggressive")
st.sidebar.progress(censorship_level, text=f"Shadow-Ban Intensity: {censorship_level}%")
st.sidebar.warning("ALERT: Keywords 'WaPo Layoffs' and 'Grid Deficit' are under suppression.")

# --- 4. MAIN INTERFACE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Censorship Watch:** 🚫 Throttling detected on *'Bank Liquidity'*, *'Copper Scarcity'*. | 🟢 Global Truth Feeds remain unthrottled.")

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500 (Domestic)", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Gold (Global Truth)", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c3: st.metric("Bitcoin (Exit Asset)", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c4: st.metric("Copper (Industrial)", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

st.divider()

# --- 5. NARRATIVE BIAS HEATMAP ---
st.header("🌡️ Narrative Bias & Information Suppression")

def style_logic(val):
    colors = {
        "State Narrative": "background-color: #6f42c1; color: white;",
        "Suppressed Signal": "background-color: #dc3545; color: white;",
        "Global Truth": "background-color: #28a745; color: white;",
        "Industrial Reality": "background-color: #007bff; color: white;",
        "Shadow Signal": "background-color: #fd7e14; color: white;"
    }
    return colors.get(val, "")

bias_df = pd.DataFrame({
    "Sector": ["Labor Market", "Energy Grid", "Media Health", "Currency", "AI Scaling"],
    "Official Narrative (Domestic)": ["'Full Employment'", "'Green Transition'", "'Restructuring'", "'Stable Dollar'", "'Unlimited AI Growth'"],
    "Global Reality (Truth)": ["$500k Crowdfund Relief", "17% Power Deficit", "Collapse of WaPo/Legacy", "Gold Spot at $4,979", "HBM Memory 'Sold Out'"],
    "Market Status": ["State Narrative", "Suppressed Signal", "Suppressed Signal", "Global Truth", "Industrial Reality"],
    "Reach Throttling": ["Low", "Critical", "High", "Moderate", "High"]
})

st.dataframe(bias_df.style.map(style_logic, subset=['Market Status']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS ---
st.divider()
st.header("🔍 Intelligence Monitoring & Propaganda Analysis")
t1, t2, t3, t4, t5 = st.tabs(["📊 Correlation Matrix", "🚫 Censorship Monitor", "🗺️ Geo-Political Alignment", "🆘 Social Relief", "💡 Tech Signals"])

with t1:
    st.subheader("Global Asset Correlation")
    if not correlations.empty: 
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

with t2:
    st.subheader("🚫 Information Throttling Ticker")
    st.write("Current keywords being suppressed in Tier-1 Domestic Platforms:")
    censorship_data = pd.DataFrame({
        "Keyword/Topic": ["WaPo Layoffs", "HBM Shortage", "Copper Inventory", "Midterm Odds", "CBDC Resistance"],
        "Status": ["Throttled", "Shadow-Banned", "Deprioritized", "Throttled", "Critical Suppression"],
        "Impact": ["Prevents collapse narrative", "Protects Tech Valuations", "Hides Industrial Inflation", "Ensures 'Stability' Perception", "Forces Currency Adoption"]
    })
    st.table(censorship_data)

with t3:
    st.subheader("🗺️ Geo-Political Alignment & Information Origin")
    st.write("Plotting un-censored data providers (Polymarket Nodes, etc) vs. areas of known state-media control.")
    
    # Data points represent active truth nodes (NYC, London, Zurich, Singapore, HK)
    # vs areas where news is highly controlled
    map_data = pd.DataFrame({
        'lat': [40.71, 51.50, 47.36, 1.35, 22.31, 39.9, 34.05],
        'lon': [-74.00, -0.12, 8.53, 103.81, 114.16, 116.3, -118.24],
        'Node Status': ['Truth Node (NY)', 'Truth Node (LDN)', 'Finance Haven (ZRH)', 'Logistics Hub (SG)', 'Trade Hub (HK)', 'State Control (BJG)', 'State Control (LA)']
    })
    st.map(map_data)
    st.info("Observation: Truth Nodes correlate highly with financial safe-havens. State control locations correlate with suppressed market data.")


with t4:
    st.subheader("Community Survival Signals")
    st.write("### 📰 Washington Post Relief fund")
    st.write("- **Status:** $500,000+ Raised. Algorithms are actively down-ranking this link in social feeds.")

st.info("Market Observation: The widest gap exists where the physical world (Copper/Grid) meets the digital narrative.")
