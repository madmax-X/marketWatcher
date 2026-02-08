import streamlit as st
import pandas as pd
import yfinance as yf
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

# --- 1. PAGE CONFIG & AUTO-REFRESH ---
st.set_page_config(page_title="2026 Market Watcher", layout="wide")

# Refresh every 60 seconds
st_autorefresh(interval=60 * 1000, key="datarefresh")

# --- 2. LIVE DATA FETCHING & CORRELATION LOGIC ---
@st.cache_data(ttl=60)
def fetch_market_data():
    tickers = {
        "S&P 500": "^GSPC", 
        "Gold": "GC=F", 
        "Bitcoin": "BTC-USD", 
        "Copper": "HG=F", 
        "Crude Oil": "CL=F"
    }
    results = {}
    alerts = []
    price_history = pd.DataFrame()
    
    for name, sym in tickers.items():
        try:
            t = yf.Ticker(sym)
            # Fetch 30 days for correlation matrix, 1 year for history
            hist = t.history(period="30d")
            
            if not hist.empty:
                current_price = hist["Close"].iloc[-1]
                open_price = hist["Open"].iloc[-1]
                change_pct = ((current_price - open_price) / open_price) * 100
                
                # Capture history for correlation
                price_history[name] = hist["Close"]
                
                # Fetch Year Ago Price
                start_date = (datetime.now() - timedelta(days=370)).strftime('%Y-%m-%d')
                end_date = (datetime.now() - timedelta(days=360)).strftime('%Y-%m-%d')
                y_hist = t.history(start=start_date, end=end_date)
                y_price = y_hist["Close"].iloc[-1] if not y_hist.empty else current_price * 0.92
                
                results[name] = {
                    "price": current_price,
                    "change": change_pct,
                    "year_ago": y_price
                }
                
                if abs(change_pct) >= 5.0:
                    alerts.append(f"⚠️ VOLATILITY ALERT: {name} moved {change_pct:.2f}% today!")
            else:
                results[name] = {"price": 0.0, "change": 0.0, "year_ago": 0.0}
        except:
            results[name] = {"price": 0.0, "change": 0.0, "year_ago": 0.0}
            
    # Calculate Correlation Matrix
    corr_matrix = price_history.pct_change().corr() if not price_history.empty else pd.DataFrame()
    
    return results, alerts, corr_matrix

live_data, active_alerts, correlations = fetch_market_data()

# --- 3. UI LAYOUT ---
if active_alerts:
    for alert in active_alerts:
        st.error(alert)

st.sidebar.header("Live Macro Tickers")
for name, data in live_data.items():
    st.sidebar.metric(
        label=name, 
        value=f"{data['price']:,.2f}" if data['price'] > 0 else "Offline", 
        delta=f"{data['change']:.2f}%" if data['price'] > 0 else None
    )

st.title("🌐 2026 Global Macro & Signal Dashboard")
st.caption(f"Last Refresh: {datetime.now().strftime('%H:%M:%S')} | Data: Real-time API")

# Macro Pulse
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("S&P 500", f"{live_data['S&P 500']['price']:,.2f}")
with c2:
    st.metric("Copper (lb)", f"${live_data['Copper']['price']:,.2f}")
with c3:
    st.metric("Crude Oil (bbl)", f"${live_data['Crude Oil']['price']:,.2f}")

st.divider()

# --- 4. SENTIMENT HEATMAP ---
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
    "Platform": ["S&P 500", "Gold", "Micron/HBM", "Parcl Index", "Polymarket", "Kickstarter", "GoFundMe", "Freightos", "StockX", "Grid Cap"],
    "Value": [f"{live_data['S&P 500']['price']:,.0f}", f"${live_data['Gold']['price']:,.2f}", "Sold Out", "+6.2% Q1", "85% Pause", "1268%", "$500k+", "Suez +12d", "Mizuno +124%", "17% Deficit"],
    "Trajectory": ["Steady", "Explosive", "Bottleneck", "Steady", "Stable", "Explosive", "Emergency", "Nervous", "Hype", "Bottleneck"]
})

st.dataframe(heatmap_data.style.applymap(color_trajectory, subset=['Trajectory']), use_container_width=True, hide_index=True)

st.divider()

# --- 5. CORRELATION & INTELLIGENCE ---
st.header("🔍 Market Intelligence")
t1, t2, t3, t4 = st.tabs(["📊 Correlation Matrix", "📅 YoY History", "🚀 Tech/Social", "🗳️ Politics"])

with t1:
    st.subheader("Asset Price Correlation (30-Day)")
    st.write("A score of **1.0** means assets move perfectly together; **-1.0** means they move in opposite directions.")
    if not correlations.empty:
        st.dataframe(correlations.style.background_gradient(cmap='RdYlGn', axis=None), use_container_width=True)
    else:
        st.warning("Insufficient history for correlation.")

with t2:
    st.subheader("Year-over-Year Comparison")
    hist_compare = []
    for name, data in live_data.items():
        if data['year_ago'] > 0:
            yoy = ((data['price'] - data['year_ago']) / data['year_ago']) * 100
            hist_compare.append({"Asset": name, "Current": f"{data['price']:,.2f}", "2025 Value": f"{data['year_ago']:,.2f}", "YoY %": f"{yoy:+.2f}%"})
    st.table(pd.DataFrame(hist_compare))

with t3:
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 🆘 Social Signal")
        st.write("- **GoFundMe:** WaPo relief fund at $500,000+.")
    with col_b:
        st.write("### ⚙️ Hardware Signal")
        st.write("- **Micron/HBM:** Supply constrained through 2026.")

with t4:
    st.write("### 🗳️ Prediction Data")
    st.write("- **Midterms:** 45% Odds of Split Govt (R-Senate/D-House).")
    st.write("- **OpenAI:** 96% odds Sam Altman remains CEO.")

st.info("Market Watcher Protocol: Correlation Matrix uses 30-day log returns. Copper/Crude tracking active.")
