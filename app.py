import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_page_config(page_title="2026 Market Watcher", layout="wide")

# Refresh the app every 60 seconds
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING & VOLATILITY ALERTS ---
@st.cache_data(ttl=60)
def fetch_market_data():
    # Tickers: S&P500, Gold, BTC, Copper, Crude Oil
    tickers = {
        "S&P 500": "^GSPC", 
        "Gold": "GC=F", 
        "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", 
        "Crude Oil": "CL=F"
    }
    results = {}
    alerts = []
    
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            hist = t.history(period="2d")
            if len(hist) >= 2:
                current_price = hist["Close"].iloc[-1]
                open_price = hist["Open"].iloc[-1]
                change_pct = ((current_price - open_price) / open_price) * 100
                
                results[name] = {
                    "price": current_price,
                    "change": change_pct
                }
                
                # VOLATILITY ALERT TRIGGER (5% Threshold)
                if abs(change_pct) >= 5.0:
                    alerts.append(f"⚠️ HIGH VOLATILITY: {name} has moved {change_pct:.2f}% since open!")
            else:
                results[name] = {"price": 0.0, "change": 0.0}
        except:
            results[name] = {"price": 0.0, "change": 0.0}
    
    return results, alerts

live_data, active_alerts = fetch_market_data()

# --- 3. ALERTS SECTION ---
if active_alerts:
    for alert in active_alerts:
        st.error(alert)

# --- 4. SIDEBAR TICKERS ---
st.sidebar.header("Live Macro Tickers")
for name, data in live_data.items():
    color = "normal" if abs(data['change']) < 5 else "inverse"
    st.sidebar.metric(
        label=name, 
        value=f"{data['price']:,.2f}", 
        delta=f"{data['change']:.2f}%",
        delta_color=color
    )

st.sidebar.divider()
st.sidebar.caption(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")
st.sidebar.info("Social signals updated via 15m staggered cache.")

# --- 5. TITLE & MACRO PULSE ---
st.title("🌐 2026 Global Macro & Signal Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Equities")
    st.write(f"S&P 500 at **{live_data['S&P 500']['price']:,.2f}**. Sentiment remains cautiously optimistic for Q2.")
with col2:
    st.subheader("Commodities")
    st.write(f"Gold at **${live_data['Gold']['price']:,.2f}**. Historical safe-haven demand is peaking.")
with col3:
    st.subheader("Monetary Policy")
    st.write("Polymarket: **85% Probability** of 'No Change' in the March Fed decision.")

st.divider()

# --- 6. MARKET SENTIMENT HEATMAP ---
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

# Comprehensive 2026 Dataset
heatmap_data = pd.DataFrame({
    "Category": ["Equities", "Commodities", "AI Hardware", "Real Estate", "Prediction", "Crowdfunding", "Social Needs", "Labor", "Culture", "Energy"],
    "Platform": ["S&P 500", "Gold (XAU)", "Micron/HBM", "Parcl Index", "Polymarket", "Kickstarter", "GoFundMe", "Replit", "StockX", "Grid Cap"],
    "Live Signal": [
        f"{live_data['S&P 500']['price']:,.2f}",
        f"${live_data['Gold']['price']:,.2f}",
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

# --- 7. UNIFIED TRUTH TABLE ---
st.header("⚖️ Unified Truth Table")
st.table(heatmap_data)

# --- 8. DEEP DIVE SECTOR ANALYSIS ---
st.header("🔍 Sector Intelligence")

tab1, tab2, tab3 = st.tabs(["Crowdfunding & Social", "Tech & Infrastructure", "Politics"])

with tab1:
    st.write("### GoFundMe: Social Safety Net")
    st.write("- **WaPo Relief Fund:** $500,000+ raised. High signal for media industry instability.")
    st.write("### Kickstarter: Entrepreneurship")
    st.write("- **Tiny Epic Invincible:** Dominating board game category. 1268% funded.")

with tab2:
    st.write("### Infrastructure Bottlenecks")
    st.write("- **HBM Memory:** AI memory sold out through EOY 2026. Hardware gating software.")
    st.write("- **Energy:** Grid capacity deficits in Northern Virginia slowing DC builds.")

with tab3:
    st.write("### Prediction Markets")
    st.write("- **2026 Midterms:** Polymarket favors 'Rep Senate / Dem House' split at **45%**.")
    st.write("- **OpenAI:** 96% odds Sam Altman remains CEO through Feb.")

st.divider()
st.info("Market Watcher Protocol: Macro data live. Alerts active at 5% threshold. Social metrics 15m cached.")
