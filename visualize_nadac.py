# visualize_nadac.py
import pandas as pd
import plotly.express as px
import textwrap
import re

def extract_dosage(desc):
    """
    Helper function to extract the milligram (MG) strength
    from the NDC description string using regular expressions.
    """
    match = re.search(r'(\d+)\s*MG', str(desc).upper())
    if match:
        return match.group(0)
    return "Unknown"

def wrap_hover_desc(text):
    """
    Helper function to wrap text at 50 characters for clean hover tooltips.
    """
    if pd.isna(text): return "N/A"
    return '<br>'.join(textwrap.wrap(str(text), width=50))

def create_nadac_scatter(df):
    """
    Accepts the cleaned NADAC dataframe, extracts dosage strengths,
    and returns a Plotly scatter chart representing real pharmacy acquisition costs.
    """
    # 1. Data Preparation
    # Use .copy() to isolate data from the Streamlit cache
    plot_df = df.copy()

    # Ensure dates are in the correct datetime format
    plot_df['effective_date'] = pd.to_datetime(plot_df['effective_date'])

    # Extract Dosage and sort
    plot_df['Dosage'] = plot_df['ndc_description'].apply(extract_dosage)
    plot_df = plot_df.sort_values(by=['Brand', 'Dosage']).reset_index(drop=True)

    # Wrap hover text
    plot_df['Hover_Description'] = plot_df['ndc_description'].apply(wrap_hover_desc)

    # 2. Visualization (Interactive Scatter Plot)
    fig = px.scatter(
        plot_df,
        x="effective_date",
        y="nadac_per_unit",
        color="Brand",
        symbol="Dosage",
        # Pass custom data directly into px.scatter so it gets grouped correctly
        custom_data=['Hover_Description', 'ndc', 'Dosage'],
        title="Real Pharmacy Acquisition Costs (NADAC) for Adalimumab Products",
        labels={
            "nadac_per_unit": "NADAC Price per Unit ($)",
            "effective_date": "Effective Date",
            "Brand": "Manufacturer / Brand",
            "Dosage": "Strength (Dosage)"
        },
        opacity=0.7
    )

    # 3. Customize hover template and increase marker size
    fig.update_traces(
        hovertemplate=(
            "<b>%{fullData.name}</b><br><br>" +
            "<b>Effective Date:</b> %{x|%B %d, %Y}<br>" +
            "<b>NADAC Price (USD):</b> %{y:$,.2f}<br>" +
            "<b>Dosage:</b> %{customdata[2]}<br>" +
            "<b>NDC:</b> %{customdata[1]}<br>" +
            "<b>Description:</b><br>%{customdata[0]}" +
            "<extra></extra>"
        ),
        marker=dict(size=9, line=dict(width=0.5, color='white'))
    )

    # 4. Refine layout aesthetics
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor='white',
        xaxis=dict(showgrid=True, gridcolor='lightgray', title="Effective Date"),
        yaxis=dict(showgrid=True, gridcolor='lightgray', tickprefix='$', title="NADAC Price ($)"),
        legend_title_text="Manufacturer / Brand"
    )

    return fig