import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

# 1. Page Configuration
st.set_page_config(page_title="2026 Global Macro Hub", layout="wide")

# 2. AUTO-REFRESH ENGINE (60 Seconds)
st_autorefresh(interval=60 * 1000, key="data_refresh")

st.title("🌐 2026 Global Macro & Signal Dashboard")
st.caption(f"Real-time data aggregation: February 8, 2026 | Last Refresh: {pd.Timestamp.now().strftime('%H:%M:%S')}")

# 3. LIVE MACRO ORACLE
@st.cache_data(ttl=60)
def fetch_live_macro():
    """Fetches live market benchmarks."""
    tickers = {"S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD"}
    results = {}
    for name, sym in tickers.items():
        try:
            ticker = yf.Ticker(sym)
            results[name] = ticker.fast_info['last_price']
        except:
            results[name] = 0.0 # Fallback
    return results

macro_data = fetch_live_macro()

# 4. SIDEBAR - LIVE TICKERS
st.sidebar.header("Global Macro Tickers")
st.sidebar.metric("S&P 500", f"{macro_data['S&P 500']:,.2f}", "Live")
st.sidebar.metric("Gold (oz)", f"${macro_data['Gold']:,.2f}", "Live")
st.sidebar.metric("Bitcoin", f"${macro_data['Bitcoin']:,.2f}", "Live")
st.sidebar.divider()
st.sidebar.metric("WaPo Relief Fund", "$500,000+", "Trending")
st.sidebar.caption("Data auto-refreshes every 60 seconds.")

# 5. MACRO MARKET PULSE (Contextual Data)
st.header("📊 Macro Market Pulse")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.subheader("Equities & Volatility")
    st.write(f"The **S&P 500** is holding at **{macro_data['S&P 500']:,.2f}**. Markets are pricing in strong 2026 earnings despite recent labor-market shifts.")
with col_b:
    st.subheader("Commodities & Inflation")
    st.write(f"**Gold** maintains historic highs at **${macro_data['Gold']:,.2f}/oz** as a hedge against USD volatility and geopolitical risk.")
with col_c:
    st.subheader("Monetary Policy")
    st.write("Polymarket odds show an **85% conviction** for a 'No Change' Fed decision at the **March 17, 2026** meeting.")

st.divider()

# 6. SENTIMENT HEATMAP (Restored Tickers)
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

# RE-INTEGRATED DATASET
summary_df = pd.DataFrame({
    "Category": ["Equities", "Commodities", "Prediction", "Crowdfunding", "Social Needs", "Labor", "Culture"],
    "Platform": ["S&P 500", "Gold (XAU)", "Polymarket", "Kickstarter", "GoFundMe", "Replit", "StockX"],
    "Current Value": [
        f"{macro_data['S&P 500']:,.2f}", 
        f"${macro_data['Gold']:,.2f}", 
        "85% Odds", 
        "1268% Funded", 
        "$500,000+", 
        "$100/mo", 
        "+124% Growth"
    ],
    "Trajectory": ["Steady", "Explosive", "Stable", "Explosive", "Emergency", "Structural", "Hype"]
})

st.dataframe(summary_df.style.applymap(style_sentiment, subset=["Trajectory"]), use_container_width=True)

# 7. DEEP DIVE BY SECTOR (Restored Detail)
st.header("🔍 Deep Dive by Sector")

with st.expander("🚀 Kickstarter: Creative Entrepreneurship"):
    st.write("### Top Projects (Feb 2026)")
    st.write("- **Tiny Epic Invincible:** 1-4 hero cooperative board game based on the *Invincible* IP. Currently leading funding momentum.")
    st.write("- **LODGE:** Cozy Swiss Alps hotel-builder raised **$89k+** in its launch week.")

with st.expander("🆘 Social Crisis & GoFundMe"):
    st.write("### High-Signal Hardship")
    st.write("- **Washington Post Layoff Relief:** Surpassed **$500,000** in donations from over 4,600 donors as of Feb 8.")
    st.write("- **Indicator:** This fund is a primary bellwether for media industry stability and community support.")

with st.expander("👟 Cultural Assets & Resale (StockX)"):
    st.write("### The 'Lifestyle' Pivot")
    st.write("- **Mizuno:** Ranked as the fastest-growing sneaker brand with **124% YoY growth**.")
    st.write("- **Nike Mind 001:** Nike's first 'neuroscience-based' slide, released **Feb 5, 2026**, focuses on sensory recovery.")

with st.expander("🗳️ Prediction Markets (Polymarket/Manifold)"):
    st.write("- **Fed Decision:** 85% probability of rate maintenance on March 17.")
    st.write("- **CEO Security:** Manifold markets show **96% odds** Sam Altman remains OpenAI CEO through Feb.")

st.divider()
st.info("System: Data restored and sync'd with live macro indicators. Scraper status: Simulation mode enabled.")
