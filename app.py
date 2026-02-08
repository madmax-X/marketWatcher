import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Signal Monitor 2026", layout="wide")
st.title("🌐 Multi-Market Truth Dashboard")
st.caption("Aggregating Financial, Creative, and Social Tickers — February 2026")

# 1. SIDEBAR - CROSS-PLATFORM TICKERS
st.sidebar.header("Live Market Tickers")
st.sidebar.metric("Polymarket #1 Vol", "47% Odds", "Manifold Meta-Market")
st.sidebar.metric("BTC High Target", "$75,000", "60% Probability")
st.sidebar.metric("Sneaker Premium", "+6% Avg", "Nike/Jordan Recovery")

# 2. CORE SIGNAL TABLE
st.header("Unified Signal Overview")
df = pd.DataFrame({
    "Market": ["Social (Play)", "Labor (Bounty)", "Cultural (Resale)", "Speculative (Real)"],
    "Platform": ["Manifold", "Replit Bounties", "StockX / GOAT", "Polymarket"],
    "Current Signal": ["Sam Altman CEO (96%)", "AI Automation Focus", "Nike 'Mind 001' Hype", "Split Midterm Congress"],
    "Trend": ["Stable", "Rising Cost", "Luxury Rebound", "Nervous"]
})
st.table(df)

# 3. EXPANDABLE CATEGORY DRILL-DOWNS
st.header("🔍 Category Deep Dives")

with st.expander("🎭 Manifold: Social & Meta-Forecasting"):
    st.write("### The Social Pulse (Feb 2026)")
    st.write("- **Meta-Predictions:** Polymarket is the **47% favorite** to lead 2026 volume, followed by Kalshi at **34%**.")
    st.write("- **Tech Odds:** There is a **96% probability** Sam Altman remains CEO through February.")
    st.write("- **Crypto Outlook:** Traders see a **75% chance** of Bitcoin dipping below $60k at some point in 2026.")

with st.expander("💻 Replit Bounties: Technical Labor Demand"):
    st.write("### AI & Dev Economy")
    st.write("- **Pricing Shift:** Replit is sunsetting 'Teams' and transitioning to a **$100/mo Pro Plan** effective Feb 20, 2026.")
    st.write("- **Labor Trends:** Focus has shifted to **Replit Agents 3.0** for building autonomous apps with integrated Stripe payments.")
    st.write("- **Task Complexity:** Minor bug fixes now cost less than the previous $0.25 fixed price, while complex builds are bundled.")

with st.expander("👟 StockX / GOAT: Cultural Assets"):
    st.write("### Secondary Market Valuation")
    st.write("- **Growth Leader:** *Mizuno* is the fastest-growing brand (up **124%**), signaling a shift toward performance-lifestyle silhouettes.")
    st.write("- **Hype Cycle:** Early 2026 is dominated by the **Nike Mind 001** and the revival of the **Nike Total 90** line.")
    st.write("- **Luxury Outlook:** The luxury footwear market is projected to reach **$44.2B** this year as sneakers become 'investment-grade' assets.")

with st.expander("🆘 GoFundMe & Polymarket (Speculative/Altruistic)"):
    st.write("- **Emergency Funds:** The 'WaPo Layoff Fund' is at **$466k**, reflecting severe media contraction [Previous Data].")
    st.write("- **Geopolitics:** Polymarket odds for a US strike on Iran by Feb 28 have dropped to **31%**.")

st.divider()
st.info("To deploy for free: Upload this app.py to GitHub and connect to Streamlit Community Cloud.")
