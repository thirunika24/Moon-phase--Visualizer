import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Moon Phase Visualizer", page_icon="🌙")

st.markdown("<h1 style='text-align: center; color: #ffffff;'>🌌 Moon Phase Visualizer</h1>", unsafe_allow_html=True)

def moon_phase(date):
    known_new_moon = datetime(2000, 1, 6)
    days = (date - known_new_moon).days
    lunations = days / 29.53058867
    phase = lunations % 1

    if phase < 0.03 or phase > 0.97:
        return "🌑 New Moon"
    elif phase < 0.22:
        return "🌒 Waxing Crescent"
    elif phase < 0.28:
        return "🌓 First Quarter"
    elif phase < 0.47:
        return "🌔 Waxing Gibbous"
    elif phase < 0.53:
        return "🌕 Full Moon"
    elif phase < 0.72:
        return "🌖 Waning Gibbous"
    elif phase < 0.78:
        return "🌗 Last Quarter"
    else:
        return "🌘 Waning Crescent"

st.markdown("### 📅 Select a Date")
user_date = st.date_input("")

if user_date:
    result = moon_phase(datetime.combine(user_date, datetime.min.time()))
    st.markdown("## ✨ Moon Phase Result")
    st.success(result)
    st.info("This is calculated based on the lunar cycle (~29.53 days)")
    st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center;'>🚀 Created by Thiru</p>", unsafe_allow_html=True)