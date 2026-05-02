# visualize_kol.py
import pandas as pd
import plotly.express as px


def create_kol_chart(df):
    """
    Accepts the KOL Mapping dataframe, extracts the top 15 publishers,
    and returns a horizontal Plotly bar chart representing the Share of Scientific Voice.
    """
    # 1. Data Preparation
    # We use .copy() to isolate the data from the Streamlit cache
    top_kols = df.head(15).copy()

    # Sort ascending so the highest value appears at the top of the horizontal chart
    top_kols = top_kols.sort_values(by="Publication_Count", ascending=True)

    # 2. Chart Creation
    fig = px.bar(
        top_kols,
        x='Publication_Count',
        y='KOL_Name',
        orientation='h',
        title="Top 15 Adalimumab Key Opinion Leaders",
        color='Publication_Count',
        color_continuous_scale='Blues'
    )

    return fig