import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Global Truth Dashboard 2026", layout="wide")
st.title("🌐 Global Market Signal Monitor (Feb 2026)")

# 2. Sidebar for Real-Time Tickers
st.sidebar.header("Live Tickers")
st.sidebar.metric("BTC Prediction", "$75,000", "60% Probability")
st.sidebar.metric("WaPo Relief Fund", "$466,976", "Trending")

# 3. Global Prediction Table
st.header("Unified Prediction Table")
data = {
    "Category": ["Politics", "Media", "Tech", "Crypto"],
    "Lead Platform": ["Polymarket", "GoFundMe", "Kickstarter", "Polymarket"],
    "Market Signal": ["Split Midterm Congress", "High Industry Layoffs", "Mecha Comet Hardware", "$75k Consolidation"],
    "Sentiment": ["Cautious", "Emergency", "Explosive", "Bullish"]
}
df = pd.DataFrame(data)
st.table(df)

# 4. Market Deep Dives
col1, col2 = st.columns(2)
with col1:
    st.subheader("🔥 Crowdfunding Hotlist (Kickstarter)")
    st.write("- **LODGE**: $89,340 raised")
    st.write("- **Sutten Mountain**: Top Collector Edition")
with col2:
    st.subheader("⚖️ High-Volume Odds (Polymarket)")
    st.write("- **Alphabet** Largest Co: 84% odds")
    st.write("- **US Strike on Iran**: 50% odds")
