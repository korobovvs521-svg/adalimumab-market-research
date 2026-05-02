# visualize_safety.py
import pandas as pd
import plotly.express as px


def create_safety_chart(df):
    """
    Accepts the Safety Profile dataframe, extracts the top reported
    adverse events, and returns a Plotly treemap figure.
    """
    # 1. Data Preparation
    # We use .copy() to prevent mutating the Streamlit cache
    top_safety = df.head(15).copy()

    # 2. Chart Creation
    fig = px.treemap(
        top_safety,
        path=['Adverse_Event'],
        values='Reported_Cases',
        color='Reported_Cases',
        color_continuous_scale='Reds',
        title="Top Reported Adverse Events for Adalimumab"
    )

    return fig