import streamlit as st
from textblob import TextBlob
st.header(" Real Time Sentiment Analyzer ")

st.image("senti22.png", width=500)
input = st.text_input(r"$\textsf{\Large Enter text here}$")


score = TextBlob(input).sentiment.polarity

if score == 0:
    st.markdown("<p style='font-family:Arial; font-size:24px'>Sentiment: Neutral 😐</p>", unsafe_allow_html=True)
elif score < 0:
    st.markdown("<p style='font-family:Arial; font-size:24px'>Sentiment: Negative 😫</p>", unsafe_allow_html=True)
elif score > 0:
    st.markdown("<p style='font-family:Arial; font-size:24px'>Sentiment: Positive 😀</p>", unsafe_allow_html=True)
