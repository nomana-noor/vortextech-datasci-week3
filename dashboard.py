import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Amazon Sales Dashboard')

df = pd.read_csv('amazon.csv')

# --- Data Cleaning (jaisa Week 1 mein kiya tha) ---
df['discounted_price'] = df['discounted_price'].str.replace('₹', '', regex=False).str.replace(',', '', regex=False).astype(float)
df['actual_price'] = df['actual_price'].str.replace('₹', '', regex=False).str.replace(',', '', regex=False).astype(float)
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=False).astype(float)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = df['rating_count'].str.replace(',', '', regex=False).astype(float)
df = df.dropna(subset=['rating', 'rating_count'])
df['main_category'] = df['category'].str.split('|').str[0]

# --- Filter 1: Dropdown for Category ---
category = st.selectbox('Select Category', df['main_category'].unique())
filtered_df = df[df['main_category'] == category]

# --- Filter 2: Slider for Price Range ---
min_price = float(filtered_df['discounted_price'].min())
max_price = float(filtered_df['discounted_price'].max())

price_range = st.slider(
    'Select Discounted Price Range (₹)',
    min_price, max_price,
    (min_price, max_price)
)

filtered_df = filtered_df[
    (filtered_df['discounted_price'] >= price_range[0]) &
    (filtered_df['discounted_price'] <= price_range[1])
]

# --- Chart 1: Rating Distribution ---
st.subheader('Rating Distribution')
fig1, ax1 = plt.subplots()
ax1.hist(filtered_df['rating'], bins=15, color='coral', edgecolor='black')
ax1.set_xlabel('Rating')
ax1.set_ylabel('Number of Products')
st.pyplot(fig1)

# --- Chart 2: Price Distribution ---
st.subheader('Discounted Price Distribution')
fig2, ax2 = plt.subplots()
ax2.hist(filtered_df['discounted_price'], bins=15, color='mediumseagreen', edgecolor='black')
ax2.set_xlabel('Discounted Price (₹)')
ax2.set_ylabel('Number of Products')
st.pyplot(fig2)

# --- Chart 3: Discount % vs Rating Scatter ---
st.subheader('Discount Percentage vs Rating')
fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df['discount_percentage'], filtered_df['rating'], alpha=0.5, color='purple')
ax3.set_xlabel('Discount Percentage (%)')
ax3.set_ylabel('Rating')
st.pyplot(fig3)

# --- Data Table ---
st.subheader('Filtered Data')
st.dataframe(filtered_df)