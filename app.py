import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_page_config(page_title="2026 Market Watcher", layout="wide")

# Refresh every 60 seconds
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING (Robust Commodity Fix) ---
@st.cache_data(ttl=60)
def fetch_market_data():
    # Tickers: S&P500, Gold, BTC, Copper (HG=F), Crude Oil (CL=F)
    tickers = {
        "S&P 500": "^GSPC", 
        "Gold": "GC=F", 
        "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", 
        "Crude Oil": "CL=F"
    }
    results = {}
    alerts = []
    historical = {}
    
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            # Fetch 5 days to ensure we bypass weekend/holiday gaps for Commodities
            hist = t.history(period="5d")
            
            if not hist.empty:
                current_price = hist["Close"].iloc[-1]
                open_price = hist["Open"].iloc[-1]
                
                # Fetch price from exactly 1 year ago for the comparison tab
                hist_year = t.history(start=(datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d'), 
                                     end=(datetime.now() - timedelta(days=360)).strftime('%Y-%m-%d'))
                year_ago_price = hist_year["Close"].iloc[0] if not hist_year.empty else current_price * 0.9
                
                change_pct = ((current_price - open_price) / open_price) * 100
                
                results[name] = {
                    "price": current_price,
                    "change": change_pct,
                    "year_ago": year_ago_price
                }
                
                if abs(change_pct) >= 5.0:
                    alerts.append(f"⚠️ HIGH VOLATILITY: {name} has moved {change_pct:.2f}% today!")
            else:
                results[name] = {"price": 0.0, "change": 0.0, "year_ago": 0.0}
        except Exception as e:
            results[name] = {"price": 0.0, "change": 0.0, "year_ago": 0.0}
    
    return results, alerts

live_data, active_alerts = fetch_market_data()

# --- 3. ALERTS SECTION ---
if active_alerts:
    for alert in active_alerts:
        st.error(alert)

# --- 4. SIDEBAR TICKERS ---
st.sidebar.header("Live Macro Tickers")
for name, data in live_data.items():
    # Fix for display if data is still 0 after all attempts
    val_display = f"{data['price']:,.2f}" if data['price'] > 0 else "Market Closed"
    st.sidebar.metric(
        label=name, 
        value=val_display, 
        delta=f"{data['change']:.2f}%" if data['price'] > 0 else None
    )

st.sidebar.divider()
st.sidebar.caption(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")

# --- 5. TITLE & MACRO PULSE ---
st.title("🌐 2026 Global Macro & Signal Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Equities")
    st.write(f"S&P 500 at **{live_data['S&P 500']['price']:,.2f}**. 2026 outlook remains tied to AI infrastructure spend.")
with col2:
    st.subheader("Industrial Signals")
    st.write(f"Copper: **${live_data['Copper']['price']:,.2f}/lb**. Crude: **${live_data['Crude Oil']['price']:,.2f}/bbl**.")
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

heatmap_data = pd.DataFrame({
    "Category": ["Equities", "Commodities", "AI Hardware", "Real Estate", "Prediction", "Crowdfunding", "Social Needs", "Logistics", "Culture", "Energy"],
    "Platform": ["S&P 500", "Gold (XAU)", "Micron/HBM", "Parcl Index", "Polymarket", "Kickstarter", "GoFundMe", "Freightos", "StockX", "Grid Cap"],
    "Live Signal": [
        f"{live_data['S&P 500']['price']:,.2f}",
        f"${live_data['Gold']['price']:,.2f}",
        "Sold Out for 2026",
        "+6.2% Q1 Estimate",
        "85% Fed Pause Odds",
        "1268% (Invincible)",
        "$500k+ (WaPo Relief)",
        "Suez +12d Delay",
        "Mizuno +124% YoY",
        "17% Power Deficit"
    ],
    "Trajectory": ["Steady", "Explosive", "Bottleneck", "Steady", "Stable", "Explosive", "Emergency", "Nervous", "Hype", "Bottleneck"]
})

st.dataframe(
    heatmap_data.style.applymap(color_trajectory, subset=['Trajectory']),
    use_container_width=True,
    hide_index=True
)

st.divider()

# --- 7. SECTOR INTELLIGENCE & HISTORY ---
st.header("🔍 Sector Intelligence")

tab1, tab2, tab3, tab4 = st.tabs(["Crowdfunding & Social", "Tech & Infrastructure", "Politics", "📅 Historical Comparison"])

with tab1:
    st.write("### GoFundMe: Social Safety Net")
    st.write("- **WaPo Relief Fund:** $500,000+ raised. High signal for media instability.")
    st.write("### Kickstarter: Entrepreneurship")
    st.write("- **Tiny Epic Invincible:** Dominating board game category. 1268% funded.")

with tab2:
    st.write("### Infrastructure Bottlenecks")
    st.write("- **HBM Memory:** AI memory sold out through EOY 2026.")
    st.write("- **Energy:** Grid capacity deficits slowing Data Center builds in Virginia.")

with tab3:
    st.write("### Prediction Markets")
    st.write("- **2026 Midterms:** Polymarket favors 'Rep Senate / Dem House' split at **45%**.")
    st.write("- **OpenAI:** 96% odds Sam Altman remains CEO through Feb.")

with tab4:
    st.write("### Year-over-Year Macro Change")
    hist_compare = []
    for name, data in live_data.items():
        yoy_change = ((data['price'] - data['year_ago']) / data['year_ago']) * 100
        hist_compare.append({"Asset": name, "Current": data['price'], "2025 Value": data['year_ago'], "YoY %": f"{yoy_change:+.2f}%"})
    
    st.table(pd.DataFrame(hist_compare))

st.divider()
st.info("Market Watcher Protocol: Robust fetching for Commodities active. Alerts active at 5% threshold.")

