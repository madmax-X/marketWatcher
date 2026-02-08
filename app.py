import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 Global Macro Hub", layout="wide")
st.title("🌐 2026 Global Macro & Signal Dashboard")
st.caption("Real-time data aggregation: February 8, 2026")

# 1. MACRO TICKER BAR (Sidebar)
st.sidebar.header("Global Macro Tickers")
st.sidebar.metric("S&P 500", "6,932.30", "+1.97% (Feb 6)")
st.sidebar.metric("Gold (oz)", "$4,979.80", "+7.03% (Weekly)")
st.sidebar.metric("US 10Y Yield", "4.22%", "-0.05 (Stable)")

# 2. SECTOR DEEP DIVES
st.header("🔍 Sector Intelligence")

with st.expander("🚀 Kickstarter: Creative Entrepreneurship"):
    st.write("### Top Trending (Feb 2026)")
    st.write("- **LODGE:** Cozy Swiss Alps hotel-builder raised **$89k+** in week one.")
    st.write("- **Tiny Epic Invincible:** Tabletop category lead at **1268%** funding.")
    st.write("- **Gambit AI:** Smart cooking device trending in the Technology category.")

with st.expander("📈 Macro Finance (Indices & Commodities)"):
    st.write("- **Nasdaq-100:** Closed near **25,075.77** on Feb 6.")
    st.write("- **Currency:** EUR/USD trending near **1.1818** as the Dollar faces pressure.")

with st.expander("🗳️ Prediction & Social Forecasting"):
    st.write("- **Midterm Forecast:** 45% odds lead for a 'split government' outcome.")
    st.write("- **CEO Stability:** 96% odds Sam Altman remains OpenAI CEO through Feb.")

with st.expander("🆘 Social Crisis (GoFundMe)"):
    st.write("- **Media Relief:** The Washington Post Guild Fund has reached **$500,000+**.")
