import streamlit as st
import pandas as pd

# PAGE CONFIG
st.set_page_config(page_title="IT Portal", layout="wide")

# SIDEBAR THEME SWITCH
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])

# THEME COLORS
if theme == "Dark":
    background = "#0E1117"
    card_bg = "#1c1f26"
    text_color = "#FFFFFF"
    desc_color = "#B0B0B0"
    shadow = "0px 6px 20px rgba(255,255,255,0.05)"
else:
    background = "#f4f6fb"
    card_bg = "#FFFFFF"
    text_color = "#1f2933"
    desc_color = "#555555"
    shadow = "0px 6px 20px rgba(0,0,0,0.1)"

# CUSTOM CSS
st.markdown(f"""
<style>

.stApp {{
background-color: {background};
}}

.portal-title {{
font-size:38px;
font-weight:700;
color:{text_color};
margin-bottom:25px;
}}

.card {{
background-color: {card_bg};
padding: 35px;
border-radius: 16px;
text-align: center;
margin-bottom: 30px;
box-shadow: {shadow};
transition: 0.3s;
height: 230px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
}}

.card:hover {{
transform: translateY(-8px);
box-shadow: 0px 12px 30px rgba(0,0,0,0.2);
}}

.card img {{
width:70px;
margin-bottom:14px;
}}

.title {{
font-size:20px;
font-weight:600;
color:{text_color};
margin-bottom:6px;
}}

.desc {{
font-size:14px;
color:{desc_color};
}}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    f"<div class='portal-title'>🌐 IT Resource Portal</div>",
    unsafe_allow_html=True
)

# LOAD EXCEL
df = pd.read_excel("websites.xlsx", engine="openpyxl")

# SEARCH
search = st.text_input("🔍 Search Tool")

if search:
    df = df[df["Name"].str.contains(search, case=False)]

# CATEGORY FILTER
category = st.selectbox(
    "Category",
    ["All"] + list(df["Category"].dropna().unique())
)

if category != "All":
    df = df[df["Category"] == category]

st.write("")

# GRID SETTINGS
cards_per_row = 3

for i in range(0, len(df), cards_per_row):

    cols = st.columns(cards_per_row, gap="large")

    for col, (_, row) in zip(cols, df.iloc[i:i+cards_per_row].iterrows()):
        with col:
            st.markdown(
                f"""
                <a href="{row['URL']}" target="_blank" style="text-decoration:none;">
                <div class="card">
                    <img src="https://www.google.com/s2/favicons?domain={row['URL']}">
                    <div class="title">{row['Name']}</div>
                    <div class="desc">{row['Description']}</div>
                </div>
                </a>
                """,
                unsafe_allow_html=True
            )