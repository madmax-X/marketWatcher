import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

# 1. Page Configuration
st.set_page_config(page_title="2026 Global Macro Hub", layout="wide")

# 2. AUTO-REFRESH (Every 60 seconds)
# This keeps the dashboard live without manual refreshes
st_autorefresh(interval=60 * 1000, key="data_refresh")

st.title("🌐 2026 Global Macro & Signal Dashboard")
st.caption(f"Real-time data aggregation: February 8, 2026 | Last Updated: {pd.Timestamp.now().strftime('%H:%M:%S')}")

# 3. LIVE DATA ORACLE
@st.cache_data(ttl=60)
def fetch_live_macro():
    """Fetches live prices from Yahoo Finance."""
    tickers = {"S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD"}
    results = {}
    for name, sym in tickers.items():
        try:
            ticker = yf.Ticker(sym)
            results[name] = ticker.fast_info['last_price']
        except:
            results[name] = 0.0
    return results

macro_data = fetch_live_macro()

# 4. SIDEBAR - REAL-TIME TICKERS
st.sidebar.header("Global Macro Tickers")
st.sidebar.metric("S&P 500", f"{macro_data['S&P 500']:,.2f}")
st.sidebar.metric("Gold (oz)", f"${macro_data['Gold']:,.2f}")
st.sidebar.metric("Bitcoin", f"${macro_data['Bitcoin']:,.2f}")
st.sidebar.divider()
st.sidebar.info("Data auto-refreshes every 60 seconds.")

# 5. MACRO MARKET PULSE
st.header("📊 Macro Market Pulse")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.subheader("Equities & Volatility")
    st.write(f"The **S&P 500** is currently at **{macro_data['S&P 500']:,.2f}**. Tech resilience remains the primary anchor for 2026 indices.")
with col_b:
    st.subheader("Commodities & Inflation")
    st.write(f"**Gold** is maintaining historic levels near **${macro_data['Gold']:,.2f}/oz** as a hedge against currency shifts.")
with col_c:
    st.subheader("Monetary Policy")
    st.write("Current consensus for March 18 FOMC is an **85% conviction** of 'No Change' in rates.")

st.divider()

# 6. SENTIMENT HEATMAP (DYNAMIC)
st.header("🌡️ Market Sentiment Heatmap")

def style_sentiment(val):
    color_map = {
        "Explosive": "background-color: #28a745; color: white;",
        "Steady": "background-color: #17a2b8; color: white;",
        "Stable": "background-color: #6c757d; color: white;",
        "Hype": "background-color: #ffc107; color: black;",
        "Nervous": "background-color: #fd7e14; color: white;",
        "Emergency": "background-color: #dc3545; color: white;"
    }
    return color_map.get(val, "")

summary_df = pd.DataFrame({
    "Category": ["Equities", "Commodities", "Prediction", "Crowdfunding", "Social Needs", "Labor", "Culture"],
    "Platform": ["S&P 500", "Gold (XAU)", "Polymarket", "Kickstarter", "GoFundMe", "Replit", "StockX"],
    "Current Value": [f"{macro_data['S&P 500']:,.2f}", f"${macro_data['Gold']:,.2f}", "85% Odds", "$89,000+", "$500,000+", "$100/mo", "+124% YoY"],
    "Trajectory": ["Steady", "Explosive", "Stable", "Explosive", "Emergency", "Structural", "Hype"]
})

st.dataframe(summary_df.style.applymap(style_sentiment, subset=["Trajectory"]), use_container_width=True)

# 7. UNIFIED TRUTH TABLE & DEEP DIVES (Retained from previous build)
st.header("⚖️ Unified Truth Table: Benchmarks vs. Signals")
st.table(summary_df[["Category", "Platform", "Current Value", "Trajectory"]])

st.header("🔍 Deep Dive by Sector")
with st.expander("🚀 Kickstarter: Creative Entrepreneurship"):
    st.write("- **LODGE:** Cozy Swiss Alps hotel-builder raised **$89k+**.")
    st.write("- **Tiny Epic Invincible:** Tabletop category lead at **1268%** funding.")
with st.expander("🗳️ Prediction Markets"):
    st.write("- **Midterm Forecast:** 45% odds lead for a 'split government' outcome.")
    st.write("- **CEO Stability:** 96% odds Sam Altman remains OpenAI CEO [Manifold].")

st.divider()
st.info("Technical Note: This app requires 'yfinance' and 'streamlit-autorefresh' in your requirements.txt.")
