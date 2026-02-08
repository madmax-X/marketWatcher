import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_page_config(page_title="2026 Market Watcher", layout="wide")
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA ORACLE & ALERTS ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC", "Gold": "GC=F", "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", "Crude Oil": "CL=F", "Nvidia": "NVDA"
    }
    results = {}
    price_history = pd.DataFrame()
    alerts = []
    
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="30d")
            if not hist.empty:
                curr = hist["Close"].iloc[-1]
                open_val = hist["Open"].iloc[-1]
                change = ((curr - open_val) / open_val) * 100
                results[name] = {"price": curr, "change": change}
                price_history[name] = hist["Close"]
                if abs(change) >= 5.0:
                    alerts.append(f"⚠️ {name} Volatility: {change:.2f}% shift!")
        except:
            results[name] = {"price": 0.0, "change": 0.0}
    
    corr = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    return results, alerts, corr

live_data, active_alerts, correlations = fetch_market_data()

# --- 3. UI: ALERTS & TICKER ---
if active_alerts:
    for alert in active_alerts: st.error(alert)

# BREAKING NEWS TICKER
st.write(f"**Breaking Headlines:** 📰 WaPo Relief Fund hits $500k | 🔋 AI Energy Gating: DC Build-outs hit non-negotiable power limits | 🏎️ Samsung expedites HBM4 delivery for Q1.")

# --- 4. SIDEBAR: FEAR & GREED + PORTFOLIO ---
st.sidebar.header("🧭 Market Sentiment Needle")
# Current F&G as of Feb 6, 2026 is 45 (Neutral)
fg_val = 45 
st.sidebar.progress(fg_val, text=f"Fear & Greed Index: {fg_val} (Neutral)")
st.sidebar.caption("0 (Extreme Fear) — 100 (Extreme Greed)")

st.sidebar.divider()
st.sidebar.header("⚖️ Portfolio Shock Simulator")
asset = st.sidebar.selectbox("Asset", list(live_data.keys()))
shock = st.sidebar.slider("Price Shock %", -20, 20, 10)
if st.sidebar.button("Calculate"):
    proj = live_data[asset]['price'] * (1 + (shock/100))
    st.sidebar.success(f"Projected {asset}: ${proj:,.2f}")

# --- 5. MAIN DASHBOARD PULSE ---
st.title("🌐 2026 Global Intelligence Dashboard")
st.caption(f"Refreshed: {datetime.now().strftime('%H:%M:%S')} | Feb 8, 2026")

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}", f"{live_data['S&P 500']['change']:.2f}%")
with c2: st.metric("Bitcoin", f"${live_data['Bitcoin']['price']:,.2f}", f"{live_data['Bitcoin']['change']:.2f}%")
with c3: st.metric("Gold", f"${live_data['Gold']['price']:,.2f}", f"{live_data['Gold']['change']:.2f}%")
with c4: st.metric("Copper", f"${live_data['Copper']['price']:,.2f}", f"{live_data['Copper']['change']:.2f}%")

st.divider()

# --- 6. HYPE vs. UTILITY HEATMAP ---
st.header("🌡️ Hype vs. Utility Sentiment")

def style_logic(val):
    colors = {
        "Hype/Bubble": "background-color: #ffc107; color: black;",
        "Industrial Utility": "background-color: #007bff; color: white;",
        "Safe Haven": "background-color: #28a745; color: white;",
        "Supply Crisis": "background-color: #dc3545; color: white;",
        "Consolidating": "background-color: #6c757d; color: white;"
    }
    return colors.get(val, "")

hype_df = pd.DataFrame({
    "Asset Class": ["Mizuno/Lifestyle", "HBM Memory", "Copper/Grid", "Gold/Silver", "U.S. Midterms", "WaPo Relief"],
    "Platform": ["StockX", "Micron/SK Hynix", "LME/Comex", "Live Spot", "Polymarket", "GoFundMe"],
    "Signal Type": ["Hype/Bubble", "Supply Crisis", "Industrial Utility", "Safe Haven", "Consolidating", "Supply Crisis"],
    "Feb 2026 Status": ["+124% Growth", "Sold Out for 2026", "Record Grid Upgrade", "Historic Highs", "45% Split Govt", "$500k+ Raised"]
})

st.dataframe(hype_df.style.map(style_logic, subset=['Signal Type']), use_container_width=True, hide_index=True)

# --- 7. INTELLIGENCE TABS ---
st.divider()
st.header("🔍 Macro Intelligence & Social Impact")
t1, t2, t3, t4 = st.tabs(["📊 Correlation Matrix", "💡 Tech Bottlenecks", "🆘 Social Impacts", "📅 YoY History"])

with t1:
    st.subheader("30-Day Correlation Matrix")
    if not correlations.empty:
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)

with t2:
    st.subheader("AI Infrastructure & Energy Gating")
    colL, colR = st.columns(2)
    with colL:
        st.write("- **HBM4 Delivery:** Samsung/SK Hynix racing to deliver by Q1 2026. NVIDIA requesting expedited HBM4 delivery.")
        st.write("- **Energy Limits:** Data centers hit 'non-negotiable' power limits. Build-outs are on hold globally.")
    with colR:
        st.progress(84, text="HBM Supply Scarcity: 84%")
        st.write("- **Chipflation:** High-margin AI chips cannibalizing legacy 'commodity' silicon for laptops/phones.")

with t3:
    st.subheader("Community & Labor Signals")
    st.write("### 📰 Washington Post Layoff Fund")
    st.write("- **Status:** Surpassed **$500,000** from **4,600+ donors**.")
    st.write("- **Impact:** Post-layoff restructuring (300+ cut) signaling permanent shift in media economics.")
    st.write("### 🚀 Kickstarter Momentum")
    st.write("- **Tiny Epic Invincible:** 1268% Funded. The 'Cozy/Boardgame' economy remains a strong consumer signal.")

with t4:
    st.subheader("Historical Context")
    st.write("- **Nike Mind 001:** Launching as the first 'neuroscience mule' for recovery. Sold out instantly.")
    st.write("- **Polymarket Meta:** 45% odds favoring a split Congress; markets are pricing in gridlock for the remainder of 2026.")

st.info("Market Observation: 2026 is the year where 'Physical Limits' (Power/Memory) finally caught up to 'Digital Speed.'")
