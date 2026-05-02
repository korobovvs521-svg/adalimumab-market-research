# visualize_wac.py
import pandas as pd
import plotly.express as px
import re
import textwrap


def get_clean_brand(row):
    """
    Helper function to extract a clean proprietary brand name
    from the product description or manufacturer name.
    """
    desc = str(row['Drug Product Description']).upper()
    manufacturer = str(row['Manufacturer Name']).upper()

    desc = re.sub(r'\(ADALIMUMAB[^)]*\)', '', desc).strip()
    parts = desc.split(' ')
    first_word = parts[0].strip(',;: ') if len(parts) > 0 else ""

    if not first_word or any(char.isdigit() for char in first_word):
        if "ABBVIE" in manufacturer: return "Humira (AbbVie)"
        if "AMGEN" in manufacturer: return "Amjevita (Amgen)"
        if "SANDOZ" in manufacturer: return "Hyrimoz (Sandoz)"
        if "BOEHRINGER" in manufacturer: return "Cyltezo (Boehringer)"
        if "ORGANON" in manufacturer: return "Hadlima (Organon)"
        if "COHERUS" in manufacturer: return "Yusimry (Coherus)"
        if "BIOCON" in manufacturer: return "Hulio (Biocon)"
        if "PFIZER" in manufacturer: return "Abrilada (Pfizer)"
        if "FRESENIUS" in manufacturer: return "Idacio (Fresenius)"
        if "CELLTRION" in manufacturer: return "Yuflyma (Celltrion)"
        return manufacturer.title()
    else:
        return first_word.capitalize()


def wrap_hover_desc(text):
    """
    Helper function to wrap text at 50 characters for clean hover tooltips.
    """
    if pd.isna(text): return "N/A"
    return '<br>'.join(textwrap.wrap(str(text), width=50))


def create_wac_chart(df):
    """
    Accepts the raw WAC history dataframe, filters for adalimumab products,
    cleans the brand names, and returns a Plotly step-line chart.
    """
    # 1. Filter and Prepare the Data
    adali_df = df[df['Drug Product Description'].str.contains('adalimumab|HUMIRA', case=False, na=False)].copy()
    adali_df['WAC Effective Date'] = pd.to_datetime(adali_df['WAC Effective Date'])

    # Apply cleaning functions
    adali_df['Brand'] = adali_df.apply(get_clean_brand, axis=1)
    adali_df['Brand'] = adali_df['Brand'].replace({'Humira': 'Humira (AbbVie)'})
    adali_df = adali_df.sort_values(by='WAC Effective Date')

    # Create the wrapped text column for the hover popup
    adali_df['Hover_Description'] = adali_df['Drug Product Description'].apply(wrap_hover_desc)

    # 2. Visualization (Step Line Chart)
    fig = px.line(
        adali_df,
        x="WAC Effective Date",
        y="WAC After Increase",
        color="Brand",
        line_shape="hv",
        markers=True,
        title="Adalimumab WAC (Wholesale Acquisition Cost) History"
    )

    # Apply the highly customized hover template
    fig.update_traces(
        hovertemplate=(
                "<b>%{fullData.name}</b><br><br>" +
                "<b>Effective Date:</b> %{x|%B %d, %Y}<br>" +
                "<b>WAC Price (USD):</b> %{y:$,.2f}<br>" +
                "<b>Description:</b><br>%{customdata[0]}" +
                "<extra></extra>"
        ),
        customdata=adali_df[['Hover_Description']]
    )

    # Refine Layout Aesthetics
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor='white',
        xaxis=dict(showgrid=True, gridcolor='lightgrey', title="Effective Date"),
        yaxis=dict(showgrid=True, gridcolor='lightgrey', tickprefix='$', title="WAC Price (USD)"),
        legend_title_text="Proprietary Name"
    )

    return fig