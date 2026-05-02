# visualize_openfda.py
import pandas as pd
import plotly.express as px
import ast
import textwrap

def clean_active(val):
    """
    Safely converts stringified JSON of active ingredients into clean text.
    """
    if pd.isna(val): return "N/A"
    try:
        items = ast.literal_eval(str(val))
        res = []
        for item in items:
            name = item.get('name', 'N/A')
            strength = item.get('strength', 'N/A')
            res.append(f"{name}, strength {strength}")
        return ", ".join(res)
    except:
        return str(val)

def clean_packaging(val):
    """
    Safely converts stringified JSON of packaging data into clean, wrapped HTML text.
    """
    if pd.isna(val): return "N/A"
    try:
        items = ast.literal_eval(str(val))
        res = []
        for item in items:
            pkg_ndc = item.get('package_ndc', 'N/A')
            desc = item.get('description', 'N/A')
            date = item.get('marketing_start_date', 'N/A')

            desc_wrapped = "<br>&nbsp;&nbsp;&nbsp;&nbsp;".join(textwrap.wrap(desc, width=50))
            res.append(f"package_ndc: {pkg_ndc},<br>&nbsp;&nbsp;&nbsp;&nbsp;description: {desc_wrapped},<br>&nbsp;&nbsp;&nbsp;&nbsp;marketing_start_date: {date}")
        return "<br>".join(res)
    except:
        return str(val)

def create_openfda_sunburst(df):
    """
    Accepts the raw OpenFDA dataframe, parses nested JSON columns,
    builds highly detailed hover tooltips, and returns a Plotly Sunburst chart.
    """
    # 1. Data Preparation
    plot_df = df.copy()
    plot_df = plot_df.dropna(subset=['labeler_name', 'generic_name', 'product_ndc'])
    plot_df['finished'] = plot_df['finished'].astype(str)

    plot_df['Clean_Active'] = plot_df['active_ingredients'].apply(clean_active)
    plot_df['Clean_Packaging'] = plot_df['packaging'].apply(clean_packaging)

    # 2. Create detailed hover text
    plot_df['Hover_Text'] = (
            "<b>product_ndc:</b> " + plot_df['product_ndc'] + "<br>" +
            "<b>generic_name:</b> " + plot_df['generic_name'] + "<br>" +
            "<b>labeler_name:</b> " + plot_df['labeler_name'] + "<br>" +
            "<b>Active ingredients:</b> " + plot_df['Clean_Active'] + "<br>" +
            "<b>finished:</b> " + plot_df['finished'] + "<br>" +
            "<b>Packaging:</b><br> " + plot_df['Clean_Packaging']
    )

    ndc_hover_dict = dict(zip(plot_df['product_ndc'], plot_df['Hover_Text']))

    # 3. Chart Creation
    fig = px.sunburst(
        plot_df,
        path=['labeler_name', 'generic_name', 'product_ndc'],
        color='labeler_name',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        title='The Adalimumab Biosimilar Market Ecosystem in the US (Based on open source: openFDA)'
    )

    # 4. Overhaul hovertemplate logic
    hovertexts = []
    for label in fig.data[0].labels:
        if label in ndc_hover_dict:
            hovertexts.append(ndc_hover_dict[label])
        else:
            hovertexts.append(f"<span style='font-size: 16px'><b>{label}</b></span>")

    fig.update_traces(
        hovertext=hovertexts,
        hovertemplate="%{hovertext}<extra></extra>"
    )

    # 5. Refine Layout
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=80, l=20, r=20, b=20),
        height=800,
        autosize=True
    )

    return fig