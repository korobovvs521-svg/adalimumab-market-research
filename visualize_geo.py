# visualize_geo.py
import pandas as pd
import plotly.express as px


def create_geo_map(df):
    """
    Accepts the Global Footprint dataframe, maps trial density by country,
    and returns a highly customized Plotly scatter_geo figure.
    """
    # 1. Data Preparation
    # We use .copy() to prevent mutating the Streamlit cache
    plot_df = df.copy()

    # 2. Chart Creation
    fig = px.scatter_geo(
        plot_df,
        locations="Country",
        locationmode="country names",
        size="Trial_Count",
        hover_name="Country",
        color="Trial_Count",
        color_continuous_scale="YlOrRd",
        projection="robinson",
        size_max=35
    )

    # 3. Refine Aesthetics (High-res borders, distinct land/ocean contrast)
    fig.update_geos(
        showcountries=True, countrycolor="#D1D5DB",
        showland=True, landcolor="#F3F4F6",
        showocean=True, oceancolor="#FFFFFF",
        coastlinecolor="#D1D5DB",
        resolution=50
    )

    # Add a dark red border to markers for maximum contrast against the light map
    fig.update_traces(
        marker=dict(line=dict(width=1.2, color='#8B0000'), opacity=0.85)
    )

    # Tightly pack the map by removing margins
    fig.update_layout(
        margin={"r": 0, "t": 10, "l": 0, "b": 0},
        coloraxis_colorbar=dict(title="Trial Volume")
    )

    return fig