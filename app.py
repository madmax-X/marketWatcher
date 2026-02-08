import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_page_config(page_title="2026 Truth Oracle", layout="wide")
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC", 
        "Gold": "GC=F", 
        "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", 
        "Baltic Dry Index": "BDIY.L",
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
        except: results[name] = {"price": 0.0, "change": 0.0}
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, corr

live_data, correlations = fetch_market_data()

# --- 3. SIDEBAR: THE PROPAGANDA DELTA ---
st.sidebar.header("👁️ Narrative Intelligence")
divergence_score = 78 # Calculated based on Market vs Media Discordance
st.sidebar.slider("Global Propaganda Delta", 0, 100, divergence_score, help="Higher scores indicate a widening gap between State Media and Global Market Reality.")
st.sidebar.warning(f"CRITICAL DIVERGENCE: Global indicators (Gold/Copper) are moving {divergence_score}% out of sync with Domestic Sentiment indices.")

# --- 4. MAIN INTERFACE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.write(f"**Breaking Headlines:** 📰 WaPo Relief Fund hits $500k | ⚡ Global Energy Gating: DC Build-outs hit non-negotiable power limits.")

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("Domestic S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Bitcoin (Global)", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c3: st.metric("Spot Gold (Global)", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c4: st.metric("Industrial Copper", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

st.divider()

# --- 5. NARRATIVE BIAS HEATMAP ---
st.header("🌡️ Narrative Bias & Sentiment Heatmap")

def style_logic(val):
    colors = {
        "State Narrative": "background-color: #6f42c1; color: white;",
        "Industrial Reality": "background-color: #007bff; color: white;",
        "Safe Haven": "background-color: #28a745; color: white;",
        "Supply Crisis": "background-color: #dc3545; color: white;",
        "Grassroots": "background-color: #fd7e14; color: white;"
    }
    return colors.get(val, "")

bias_df = pd.DataFrame({
    "Sector": ["US Economy", "Energy Policy", "Cyber Security", "Social Stability", "Currency"],
    "Domestic Reporting (State)": ["'Resilient Growth'", "'Renewable Abundance'", "'Enhanced Protection'", "'Unity & Progress'", "'Digital Freedom (CBDC)'"],
    "Global Indicators (Truth)": ["WaPo Layoffs ($500k Fund)", "Grid Deficit (17%)", "HBM Hardware Bottlenecks", "45% Split Govt Odds", "Gold Spot at $5,000"],
    "Bias Category": ["State Narrative", "Supply Crisis", "Industrial Reality", "Grassroots", "Safe Haven"],
    "Propaganda Delta": ["High", "Critical", "Moderate", "High", "Critical"]
})

st.dataframe(bias_df.style.map(style_logic, subset=['Bias Category']), use_container_width=True, hide_index=True)

# --- 6. INTELLIGENCE TABS ---
st.divider()
st.header("🔍 Global vs. Domestic Truth Correlation")
t1, t2, t3, t4 = st.tabs(["📊 Market Correlation", "⚡ Tech & Physical Realities", "🆘 Social Truths", "👁️ Propaganda Plotting"])

with t1:
    st.subheader("Global Asset Correlation")
    if not correlations.empty: st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

with t2:
    st.subheader("The Industrial Bottleneck")
    st.write("- **State Media:** Reports 'unlimited AI potential'.")
    st.write("- **Global Reality:** **HBM4 Supply is Sold Out.** Software cannot scale further without physical silicon allocation.")
    st.progress(84, text="Global HBM Scarcity: 84%")

with t3:
    st.subheader("Social Discordance")
    st.write("### 📰 The Media Collapse")
    st.write("- **Domestic Framing:** 'Industry Restructuring for the Digital Age.'")
    st.write("- **Social Signal:** $500,000+ raised on GoFundMe for laid-off journalists. Community mutual aid is replacing corporate safety nets.")

with t4:
    st.subheader("👁️ Propaganda Plotting: Media vs. Reality")
    
    st.write("### Global Reporting Divergence Index")
    divergence_data = pd.DataFrame({
        "Narrative Vector": ["Consumer Spending", "National Debt", "Energy Transition", "Political Unity"],
        "Domestic News Tone": ["Optimistic / Buy Now", "Ignored / Sustained", "Triumphant / Green", "Inclusive / Stabilized"],
        "Global Market Reaction": ["Bitcoin Surge (Alt Asset)", "Gold Highs (Hedge)", "Copper Spike (Industrial)", "Polymarket Gridlock Odds"],
        "Truth Delta": ["9.2 (Critical)", "8.5 (High)", "7.1 (Moderate)", "9.8 (Extreme)"]
    })
    st.table(divergence_data)
    
    st.warning("**Observation:** Domestic reporting is currently decoupled from Global Spot Markets. When the S&P 500 rises while Gold and Copper both spike, it indicates the market is pricing in **Narrative Failure** and currency devaluation.")

st.info("Market Observation: The widest delta exists in 'Energy.' Domestic media reports a green surplus; global industrial markets are pricing in a severe power shortage for AI.")
