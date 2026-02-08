import streamlit as st
import pandas as pd

st.set_page_config(page_title="2026 Global Macro Hub", layout="wide")
st.title("🌐 2026 Global Macro & Signal Dashboard")
st.caption("Real-time data aggregation: February 8, 2026")

# 1. MACRO TICKER BAR (Sidebar)
st.sidebar.header("Global Macro Tickers")
st.sidebar.metric("S&P 500", "6,932.30", "+1.97% (Feb 6)")
st.sidebar.metric("Gold (oz)", "$4,979.80", "+7.03% (Weekly)")
st.sidebar.metric("BTC Price Odds", "60% for $75k", "Moderate Bullish")

# 2. UNIFIED PREDICTION TABLE
st.header("Unified Truth Table: Benchmarks vs. Signals")
df = pd.DataFrame({
    "Domain": ["Monetary Policy", "Entrepreneurship", "Social Crisis", "Labor Tech", "Cultural Assets"],
    "Platform": ["Polymarket", "Kickstarter", "GoFundMe", "Replit Bounties", "StockX"],
    "Live Signal": ["85% Odds: No Fed Change", "LODGE: $89k+ Raised", "WaPo Relief: $500k+", "$100/mo AI Pro Pivot", "Mizuno: +124% Growth"],
    "Outlook": ["Stable", "Explosive (Cozy)", "Emergency", "Consolidating", "Explosive"]
})
st.table(df)

# 3. DETAILED MARKET DRILL-DOWNS
st.header("🔍 Deep Dive by Sector")

with st.expander("🚀 Kickstarter: Creative Entrepreneurship"):
    st.write("### Top Trending (Feb 2026)")
    st.write("- **LODGE:** A cozy hotel-builder set in the Swiss Alps, raised **$89k+** in its first week.")
    st.write("- **Tiny Epic Invincible:** Leading the tabletop category with over **1268%** funding.")
    st.write("- **Stellar Ventures:** Interstellar corporate strategy game currently among most funded.")
    st.write("- **Gambit AI:** An AI 'sous chef' device mounting over stoves, trending in the Technology category.")

with st.expander("📈 Macro Finance (Indices & Commodities)"):
    st.write("- **Nasdaq-100:** Closed near **25,075.77** on Feb 6.")
    st.write("- **Gold Highs:** Dollar weakness is driving a historic gold rally toward **$5k/oz**.")

with st.expander("🗳️ Prediction & Social Forecasting"):
    st.write("- **Midterm Forecast:** 45% odds lead for a 'split government' outcome in 2026 Midterms.")
    st.write("- **CEO Stability:** 96% odds Sam Altman remains OpenAI CEO through Feb [Manifold Signal].")

with st.expander("🆘 Social Crisis (GoFundMe)"):
    st.write("- **Media Relief:** The Washington Post Guild Fund has reached **$500,000+** to support hundreds of laid-off staff.")
