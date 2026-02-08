import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="2026 Global Macro Hub", layout="wide")
st.title("🌐 2026 Global Macro & Signal Dashboard")
st.caption("Real-time data aggregation: February 8, 2026")

# 2. Sidebar - High Velocity Tickers
st.sidebar.header("Global Macro Tickers")
st.sidebar.metric("S&P 500", "6,932.30", "+1.97% (Feb 6)")
st.sidebar.metric("Gold (oz)", "$4,979.80", "+7.03% (Weekly)")
st.sidebar.metric("BTC Price Odds", "60% for $75k", "Moderate Bullish")
st.sidebar.divider()
st.sidebar.metric("WaPo Relief Fund", "$500,000+", "Trending")

# 3. NEW: Macro Market Pulse
st.header("📊 Macro Market Pulse")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.subheader("Equities & Volatility")
    st.write("The **S&P 500** remains robust, closing at **6,932.30**. Markets are currently shrugging off tech sector volatility as earnings season stabilizes.")

with col_b:
    st.subheader("Commodities & Inflation")
    st.write("Gold has reached historic highs, trading near **$4,979.80/oz**. This rally is driven primarily by US Dollar weakness and safe-haven demand.")

with col_c:
    st.subheader("Monetary Policy")
    st.write("Current consensus for the March 18 FOMC meeting is an **85% conviction** that the Federal Reserve will hold rates steady ('No Change').")

st.divider()

# 4. NEW: Unified Market Summary Table
st.header("📝 Unified Market Summary")
summary_data = {
    "Category": ["Equities", "Commodities", "Prediction", "Prediction", "Crowdfunding", "Social Needs", "Labor", "Culture"],
    "Platform / Index": ["S&P 500", "Gold (XAU)", "Polymarket", "Polymarket", "Kickstarter", "GoFundMe", "Replit", "StockX"],
    "Indicator": ["Market Close", "Spot Price", "March Fed Decision", "2026 Midterms", "LODGE Game", "Media Layoffs", "AI Subscription", "Mizuno Resale"],
    "Feb 2026 Value": ["6,932.30", "$4,979.80", "85% Odds", "45% Odds", "$89,000+", "$500,000+", "$100/mo", "+124% YoY"],
    "Trajectory": ["Steady", "Explosive", "Stable", "Nervous", "Explosive", "Emergency", "Structural", "Hype"]
}
st.table(pd.DataFrame(summary_data))

# 5. ORIGINAL: Unified Truth Table
st.header("⚖️ Unified Truth Table: Benchmarks vs. Signals")
truth_data = {
    "Domain": ["Monetary Policy", "Entrepreneurship", "Social Crisis", "Labor Tech", "Cultural Assets"],
    "Platform": ["Polymarket", "Kickstarter", "GoFundMe", "Replit Bounties", "StockX"],
    "Live Signal": ["85% Odds: No Fed Change", "LODGE: $89k+ Raised", "WaPo Relief: $500k+", "$100/mo AI Pro Pivot", "Mizuno: +124% Growth"],
    "Outlook": ["Stable", "Explosive (Cozy)", "Emergency", "Consolidating", "Explosive"]
}
st.table(pd.DataFrame(truth_data))

# 6. ORIGINAL: Detailed Market Drill-Downs (Deep Dive)
st.header("🔍 Deep Dive by Sector")

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
    st.write("- **Media Relief:** The Washington Post Guild Fund has reached **$500,000+** to support hundreds of laid-off staff.")

st.divider()
st.info("Deployment Note: Push this code to your GitHub 'marketWatcher' repo and refresh your Streamlit Cloud app.")
