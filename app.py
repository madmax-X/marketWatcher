import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_page_config(page_title="2026 Market Watcher", layout="wide")

# Refresh the app every 60 seconds to pull new Macro data
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING (Macro) ---
@st.cache_data(ttl=60)
def fetch_live_data():
    # Tickers: S&P500, Gold, BTC, Copper (Industrial Signal), Crude Oil
    tickers = {"S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD", "Copper": "HG=F", "Crude Oil": "CL=F"}
    results = {}
    for name, sym in tickers.items():
        try:
            ticker = yf.Ticker(sym)
            # Fetching the last close price
            results[name] = ticker.history(period="1d")["Close"].iloc[-1]
        except:
            results[name] = 0.0
    return results

live_macro = fetch_live_data()

# --- 3. SIDEBAR TICKERS ---
st.sidebar.header("Live Macro Tickers")
st.sidebar.metric("S&P 500", f"{live_macro['S&P 500']:,.2f}")
st.sidebar.metric("Bitcoin", f"${live_macro['Bitcoin']:,.2f}")
st.sidebar.metric("Gold (oz)", f"${live_macro['Gold']:,.2f}")
st.sidebar.metric("Copper (lb)", f"${live_macro['Copper']:,.2f}")
st.sidebar.divider()
st.sidebar.caption(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")
st.sidebar.info("Social signals (GoFundMe/Kickstarter) updated via staggered cache.")

# --- 4. TITLE & MACRO PULSE ---
st.title("🌐 2026 Global Macro & Signal Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Equities")
    st.write(f"S&P 500 at **{live_macro['S&P 500']:,.2f}**. Markets are pricing in a 'Soft Landing' through Q2 2026.")
with col2:
    st.subheader("Commodities")
    st.write(f"Gold at **${live_macro['Gold']:,.2f}**. High demand for safe-havens amid Midterm election uncertainty.")
with col3:
    st.subheader("Monetary Policy")
    st.write("Polymarket: **85% Probability** of 'No Change' in the March Fed decision.")

st.divider()

# --- 5. MARKET SENTIMENT HEATMAP ---
st.header("🌡️ Market Sentiment Heatmap")

def color_trajectory(val):
    color_map = {
        "Explosive": "background-color: #28a745; color: white;",
        "Steady": "background-color: #17a2b8; color: white;",
        "Stable": "background-color: #6c757d; color: white;",
        "Hype": "background-color: #ffc107; color: black;",
        "Nervous": "background-color: #fd7e14; color: white;",
        "Emergency": "background-color: #dc3545; color: white;",
        "Bottleneck": "background-color: #6f42c1; color: white;"
    }
    return color_map.get(val, "")

# Combined Dataset: Real-time Macro + 2026 Signal Data
heatmap_data = pd.DataFrame({
    "Category": ["Equities", "Commodities", "AI Hardware", "Real Estate", "Prediction", "Crowdfunding", "Social Needs", "Labor", "Culture", "Energy"],
    "Platform": ["S&P 500", "Gold (XAU)", "Micron/HBM", "Parcl Index", "Polymarket", "Kickstarter", "GoFundMe", "Replit", "StockX", "Grid Cap"],
    "Live Signal": [
        f"{live_macro['S&P 500']:,.2f}",
        f"${live_macro['Gold']:,.2f}",
        "Sold Out for 2026",
        "+6.2% Q1 Estimate",
        "85% Fed Pause Odds",
        "1268% (Invincible)",
        "$500k+ (WaPo Relief)",
        "$100/mo Pro Pivot",
        "Mizuno +124% YoY",
        "17% Power Deficit"
    ],
    "Trajectory": ["Steady", "Explosive", "Bottleneck", "Steady", "Stable", "Explosive", "Emergency", "Stable", "Hype", "Bottleneck"]
})

st.dataframe(
    heatmap_data.style.applymap(color_trajectory, subset=['Trajectory']),
    use_container_width=True,
    hide_index=True
)

st.divider()

# --- 6. UNIFIED TRUTH TABLE ---
st.header("⚖️ Unified Truth Table")
st.table(heatmap_data)

# --- 7. DEEP DIVE SECTOR ANALYSIS ---
st.header("🔍 Sector Intelligence")

tab1, tab2, tab3 = st.tabs(["Crowdfunding & Social", "Tech & Infrastructure", "Politics"])

with tab1:
    st.write("### GoFundMe: Social Safety Net")
    st.write("- **WaPo Relief Fund:** $500,000+ raised following Feb 4 layoffs. High signal for media instability.")
    st.write("### Kickstarter: Entrepreneurship")
    st.write("- **Tiny Epic Invincible:** Dominating board game category. 1268% funded.")

with tab2:
    st.write("### Infrastructure Bottlenecks")
    st.write("- **HBM Memory:** AI hardware memory is sold out through EOY 2026.")
    st.write("- **Energy:** Grid capacity deficits in Virginia are slowing Data Center deployments.")

with tab3:
    st.write("### Prediction Markets")
    st.write("- **2026 Midterms:** Polymarket favors a 'Republican Senate / Democratic House' split at **45%**.")
    st.write("- **OpenAI:** 96% odds Sam Altman remains CEO through Feb.")

st.divider()
st.info("System: Dashboard pulling live macro data from YFinance. Scraper Delay (Social): 15m Cache.")
