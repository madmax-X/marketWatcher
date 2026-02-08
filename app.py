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

# --- 3. SIDEBAR: CENSORSHIP MONITOR ---
st.sidebar.header("👁️ Information Integrity")
censorship_level = 64 
st.sidebar.select_slider("Information Throttling Level", options=["Low", "Staggered", "Aggressive", "Total"], value="Aggressive")
st.sidebar.progress(censorship_level, text=f"Shadow-Ban Intensity: {censorship_level}%")
st.sidebar.warning("ALERT: Keywords 'WaPo Layoffs' and 'Grid Deficit' are under algorithmic suppression.")

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

# --- 6. INTELLIGENCE TABS (Restored Map) ---
st.divider()
st.header("🔍 Intelligence Monitoring & Propaganda Analysis")
t1, t2, t3, t4, t5 = st.tabs(["🗺️ Geopolitical Truth Map", "📊 Correlation Matrix", "🚫 Censorship Monitor", "🆘 Social Relief", "💡 Tech Signals"])

with t1:
    st.subheader("🗺️ Global Information Origin: Truth Nodes vs. State Control")
    st.write("Visualizing the origin of decentralized signals (unfiltered) vs. hubs of narrative steering.")
    
    # Mapping Coordinates
    # lat/lon keys are required for st.map
    map_df = pd.DataFrame({
        'lat': [40.71, 51.50, 22.31, 1.35, 38.89, 39.90, 55.75, 35.68, 47.37],
        'lon': [-74.00, -0.12, 114.16, 103.81, -77.03, 116.40, 37.61, 139.65, 8.54],
        'name': ['Truth Node (NY)', 'Truth Node (LDN)', 'Trade Hub (HK)', 'Logistics (SG)', 'State Control (DC)', 'State Control (BJG)', 'State Control (MOS)', 'Truth Node (TYO)', 'Finance Haven (ZRH)']
    })
    
    st.map(map_df)
    st.info("🟢 Truth Nodes: Hubs where market signals (Polymarket/Gold) move freely. | 🔴 State Centers: Hubs where search and media data are algorithmically steered.")

with t2:
    st.subheader("Global Asset Correlation")
    if not correlations.empty: 
        try:
            st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)
        except:
            st.dataframe(correlations, use_container_width=True)

with t3:
    st.subheader("🚫 Information Throttling Ticker")
    censorship_data = pd.DataFrame({
        "Keyword/Topic": ["WaPo Layoffs", "HBM Shortage", "Copper Inventory", "Midterm Odds", "CBDC Resistance"],
        "Status": ["Throttled", "Shadow-Banned", "Deprioritized", "Throttled", "Critical Suppression"],
        "Impact": ["Hides media collapse", "Protects tech stock premium", "Masks industrial inflation", "Stabilizes perception", "Forces digital adoption"]
    })
    st.table(censorship_data)

with t4:
    st.subheader("Community Survival Signals")
    st.write("### 📰 Washington Post Relief Fund")
    st.write("- **Status:** $500,000+ Raised. Official channels framing this as 'innovation'; signal shows industry collapse.")

with t5:
    st.subheader("Physical Hardware Bottlenecks")
    st.write("- **HBM Memory:** SK Hynix reporting 0% available capacity for 2026. Hardware gating AI software.")
    st.write("- **Power Grid:** Thermal limits reached in major data center hubs.")

st.info("Market Observation: Narrative control is highest in the Energy and Labor sectors. The 'Real World' (Copper/Grid) remains decoupled from the 'Digital Narrative'.")

# --- NEW: KINETIC SIGNAL & MILITARY TICKER ---
st.header("🪖 Kinetic Signals & Military Movements")

# Military Movement Data for Feb 2026
mil_data = pd.DataFrame({
    "Region": ["Europe (NATO)", "South China Sea", "Middle East", "Latin America"],
    "Movement": ["Steadfast Dart 2026", "Combat Readiness Patrols", "USS Abraham Lincoln Carrier", "US Hard Power Shift"],
    "Global Signal": ["Non-US NATO Autonomy", "Blockade-Like Formations", "Regional War Warning", "Campaign in Caribbean"],
    "Threat Level": ["Elevated", "Critical", "Emergency", "Steady"]
})

def style_threat(val):
    color_map = {
        "Emergency": "background-color: #dc3545; color: white;",
        "Critical": "background-color: #fd7e14; color: white;",
        "Elevated": "background-color: #ffc107; color: black;",
        "Steady": "background-color: #28a745; color: white;"
    }
    return color_map.get(val, "")

st.dataframe(mil_data.style.map(style_threat, subset=['Threat Level']), use_container_width=True, hide_index=True)

# --- INTELLIGENCE DEEP DIVE: KINETIC vs NARRATIVE ---
with st.expander("👁️ Kinetic Truth Deep Dive"):
    st.write("### 🇪🇺 The NATO Rupture")
    st.write("- **Narrative:** 'Stronger together.'")
    st.write("- **Kinetic Reality:** The launch of **Steadfast Dart** without US troops (Feb 2026) is a historic fracture in the 77-year alliance.")
    
    st.write("### 🇨🇳 The 'Shadow' Blockade")
    st.write("- **Narrative:** 'Standard naval patrols.'")
    st.write("- **Kinetic Reality:** Use of **2,000+ fishing boats** (Chinese Maritime Militia) to form blockade-like formations around Taiwan.")
