# VortexTech Week 3 - Interactive Amazon Sales Dashboard

## What I Built
An interactive Streamlit dashboard for exploring the Amazon Sales Dataset. Users can filter products by category and price range, and view 3 visualizations plus a data table that update automatically based on the selected filters.

## Features
- **Dropdown filter**: Select a product category
- **Slider filter**: Select a discounted price range
- **3 visualizations**: Rating distribution, discounted price distribution, and discount percentage vs rating scatter plot
- **Data table**: View the filtered raw data

## How to Run
1. Install the required libraries:
   pip install streamlit pandas matplotlib seaborn
3. Make sure `dashboard.py` and `amazon.csv` are in the same folder
4. Run the dashboard:
   streamlit run dashboard.py
5. The dashboard will open automatically in your browser
